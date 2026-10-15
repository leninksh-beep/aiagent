import os
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a Python file with optional command-line arguments relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to run, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional list of command-line arguments to pass to the script",
                },
            },
            "required": ["file_path"],
        },
    },
}

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        # 1. Resolve absolute path of working directory
        working_dir_abs = os.path.abspath(working_directory)

        # 2. Construct and normalize target path
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # 3. Guardrail: ensure target remains within working directory boundary
        valid_target_path = (
            os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
        )
        if not valid_target_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # 4. Check that target file exists and is a regular file
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        # 5. Ensure the file has a .py extension
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        # 6. Build the base command list
        command = ["python", target_path]

        # 7. Add additional arguments if provided
        if args:
            command.extend(args)

        # 8. Run the command using subprocess.run
        completed_process = subprocess.run(
            command,
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
            timeout=30,
        )

        # 9. Format output string
        output_parts = []

        if completed_process.returncode != 0:
            output_parts.append(
                f"Process exited with code {completed_process.returncode}"
            )

        stdout = completed_process.stdout
        stderr = completed_process.stderr

        if not stdout and not stderr:
            output_parts.append("No output produced")
        else:
            if stdout:
                output_parts.append(f"STDOUT:\n{stdout}")
            if stderr:
                output_parts.append(f"STDERR:\n{stderr}")

        return "\n".join(output_parts)

    except Exception as e:
        return f"Error: executing Python file: {e}"
