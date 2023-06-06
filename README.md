### Files
- `main.py`: This script allows the user to enter an expression and evaluates it using the syntax tree.
- `syntax_tree.py`: This module contains the implementation of the syntax tree and the evaluation logic.
- `Test.py/`: You can provide your own test cases by creating text files with name `Testcase{N}` where `N` is {1,2,3.....}. Each line in the file should contain a separate expression to evaluate. The program will iterate through the files and evaluate each expression, displaying the result or any errors encountered.


### Single Expression Evaluation
1. Run the `main.py` script: `python main.py`
2. Enter an expression when prompted.
3. The script will evaluate the expression using the syntax tree and display the result.

### Multiple Expressions Evaluation
1. Place your test case files in the same directory of Test.py. Each test case file should contain one expression per line.
2. Run the `Test.py` script: `python Test.py`
3. The script will automatically read each test case file and evaluate the expressions one by one, displaying the results.

Note: Test case files should have a `.txt` extension and be placed directly inside the same/current directory.
