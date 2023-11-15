import sys
from RedBlackTree import RedBlackTree

from supportFunctions import *
    
@trackExecutionTime
def main():
    # Check if a filename is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    # Get the filename from the command line argument
    input_filename = sys.argv[1]
    # Compute the filename of outputfile
    output_filename = f"{input_filename.split('.')[0]}_output_file.txt"
    rb_tree = RedBlackTree()
    function_map = {"PrintBook":rb_tree.PrintBook, "PrintBooks":rb_tree.PrintBooks, "InsertBook": rb_tree.InsertBook, "BorrowBook":rb_tree.BorrowBook, "ReturnBook":rb_tree.ReturnBook, "DeleteBook":rb_tree.DeleteBook, "FindClosestBook": rb_tree.FindClosestBook, "ColorFlipCount":rb_tree.ColorFlipCount,  "Quit":rb_tree.Quit }

    # try:
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        # Read Input Commands line by line
        for command in input_file:
            function = command.strip().split("(")[0]
            parameters = command.strip().split("(")[1].replace('"', '')[:-1].strip(")").split(", ")
            if parameters == ['']:
                parameters=[]
            # Perform required function
            op= function_map[function](*parameters)
            
            # Write function output to file
            output_file.write(f"{op}")
    # except FileNotFoundError:
    #     print(f"Error: File '{input_filename}' not found.")
    # except Exception as e:
    #     print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
