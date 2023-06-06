from syntax_tree import evaluate_expression
import os
def evaluate_test_cases(filename):
    
    with open(filename, 'r') as file:
        for line in file:
            expression = line.strip()
            try:
                result = evaluate_expression(expression)
                print("Expression:", expression)
                print("Result:", result)
                print()  # Empty line for readability
            except ValueError as e:
                print("Expression:", expression)
                print("Error:", str(e))
                print()  # Empty line for readability
            except Exception as e:
                print("Expression:", expression)
                print("Error: Invalid input")
                print()  # Empty line for readability
def main():
    
    files = os.listdir(".")  # List all files in the current directory
    i = 1
    for file in files:
        if file.endswith(".txt"):
            print(file)
            evaluate_test_cases(f"Testcase{i}.txt")
            i += 1


if __name__ == "__main__":
    main()
