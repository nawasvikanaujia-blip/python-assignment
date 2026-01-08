user_input = input("Enter some data: ")


with open("output.txt", "w") as fh:
    fh.write("User input: " + user_input + "\n")


with open("output.txt", "a") as fh:
    fh.write("Appended data: This is additional information.\n")


with open("output.txt", "r") as fh:
    print("\nFinal content of the file:")
    print(fh.read())
