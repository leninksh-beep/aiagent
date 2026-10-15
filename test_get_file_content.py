from functions.get_file_content import get_file_content


def main() -> None:
    # 1. Truncation test
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")

    # 2. Valid file reads
    print(get_file_content("calculator", "main.py"))
    print(get_file_content("calculator", "pkg/calculator.py"))

    # 3. Security boundary error test
    print(get_file_content("calculator", "/bin/cat"))

    # 4. Non-existent file error test
    print(get_file_content("calculator", "pkg/does_not_exist.py"))


if __name__ == "__main__":
    main()
