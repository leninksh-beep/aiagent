from functions.write_file import write_file


def main():
    # Test case 1: Overwriting/writing to a file in the root working directory
    res1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(res1)

    # Test case 2: Writing to a file in a subfolder (creates 'pkg/' if missing)
    res2 = write_file(
        "calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"
    )
    print(res2)

    # Test case 3: Attempting to write outside working directory
    res3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(res3)


if __name__ == "__main__":
    main()
