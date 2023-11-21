import sys
import time
from RedBlackTree import RedBlackTree

#  Wrapper function that calculates execution time of the function decorated with it
def trackExecutionTime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Total Execution Time: {execution_time:.4f} seconds")
        return result
    return wrapper
   
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

    try:
        with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
            # Read Input Commands line by line
            for command in input_file:
                function,parameters = command.strip().split("(")
                parameters = parameters.replace('"', '')[:-1].strip(")").strip(" ").split(",")
                if parameters == ['']:
                    parameters=[]
                # Perform required function
                print(command)
                op= function_map[function](*parameters)
            
                print(rb_tree.ColorFlipCount())
                
                # Write function output to file
                output_file.write(f"{op}")
                if op=="Program Terminated!!":
                    break
                
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
