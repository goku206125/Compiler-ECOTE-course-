from syntax_tree import evaluate_expression
def main():
    expression = input("Enter an expression: ")
    try:
        result = evaluate_expression(expression)
        print("Result: ", result)
    except ValueError as e:
        print(str(e))
    except Exception as e:
        print("Invalid input error")


if __name__ == "__main__":
    main()