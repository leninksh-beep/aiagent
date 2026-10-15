from functions.run_python_file import run_python_file


def main():
    print("--- Test 1: Run main.py with no args ---")
    res1 = run_python_file("calculator", "main.py")
    print(res1)
    print("\n" + "=" * 50 + "\n")

    print("--- Test 2: Run main.py with expression argument ---")
    res2 = run_python_file("calculator", "main.py", ["3 + 5"])
    print(res2)
    print("\n" + "=" * 50 + "\n")

    print("--- Test 3: Run calculator tests ---")
    res3 = run_python_file("calculator", "tests.py")
    print(res3)
    print("\n" + "=" * 50 + "\n")

    print("--- Test 4: Path traversal attempt ---")
    res4 = run_python_file("calculator", "../main.py")
    print(res4)
    print("\n" + "=" * 50 + "\n")

    print("--- Test 5: Non-existent file ---")
    res5 = run_python_file("calculator", "nonexistent.py")
    print(res5)
    print("\n" + "=" * 50 + "\n")

    print("--- Test 6: Non-python file (.txt) ---")
    res6 = run_python_file("calculator", "lorem.txt")
    print(res6)


if __name__ == "__main__":
    main()
