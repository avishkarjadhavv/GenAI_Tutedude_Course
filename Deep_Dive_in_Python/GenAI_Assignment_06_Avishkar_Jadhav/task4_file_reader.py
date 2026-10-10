
try:
    filename = input("Enter filename: ")

    with open(filename, "r") as file:
        lines = file.readlines()

    print("First 3 lines of the file:")
    for line in lines[:3]:
        print(line, end="")

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

finally:
    print("File operation attempted.")
