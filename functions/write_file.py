import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes or overwrites content to a specified file relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to write to, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "Text content to write into the file",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}

def write_file(working_directory: str, file_path: str, content: str) -> str:
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
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # 4. Check if target path points to an existing directory
        if os.path.isdir(target_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        # 5. Extract parent directory and create it if missing
        parent_dir = os.path.dirname(target_path)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)
        # 6. Open file in write mode and overwrite content
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(content)
        # 7. Return success message
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
