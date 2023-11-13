import sys

def read_and_print_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File Content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if a filename is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    # Get the filename from the command line argument
    filename = sys.argv[1]

    # Read and print the content of the file
    read_and_print_file(filename)
