class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def is_operand(self):# Check if the node is an operand (numeric value)
        return not self.is_operator()

    def is_operator(self):# Check if the node is an operator
        return self.value in ('+', '-', '*', '/', '<', '>', '==', '!=', '&&', '||', '<=', '>=')

    def evaluate(self): # Evaluate the node's value based on its operands and operator
        if self.is_operand():
            return int(self.value)# Convert the operand to an integer
        left_val = self.left.evaluate()
        right_val = self.right.evaluate()

        if self.value == '+':
            return left_val + right_val
        elif self.value == '-':
            return left_val - right_val
        elif self.value == '*':
            return left_val * right_val
        elif self.value == '/':
            if right_val == 0:
                raise ValueError("Division by zero error")
            return left_val // right_val
        elif self.value == '<':
            return int(left_val < right_val)
        elif self.value == '>':
            return int(left_val > right_val)
        elif self.value == '<=':
            return int(left_val <= right_val)
        elif self.value == '>=':
            return int(left_val >= right_val)
        elif self.value == '==':
            return int(left_val == right_val)
        elif self.value == '!=':
            return int(left_val != right_val)
        elif self.value == '&&':
            return int(bool(left_val) and bool(right_val))
        elif self.value == '||':
            return int(bool(left_val) or bool(right_val))
def tokenize(expression):#function takes an expression as input and breaks it down into tokens
    '''It iterates over each character in the expression and 
    constructs tokens based on digits, operators, parentheses, and whitespace.
    '''
    tokens = []
    current_token = ''
    i = 0
    while i < len(expression):
        c = expression[i]
        if c.isdigit() or c == '.':
            current_token += c
        elif c in ('+', '-', '*', '/', '<', '>', '=', '!', '&', '|'):
            if current_token:
                tokens.append(current_token)
                current_token = ''
            if c in ('<', '>', '=', '!', '&', '|'):
                next_char = expression[i + 1] if i + 1 < len(expression) else ''
                if next_char in ('=', '&', '|'):
                    tokens.append(c + next_char)
                    i += 1
                else:
                    tokens.append(c)
            else:
                tokens.append(c)
        elif c == ' ':
            if current_token:
                tokens.append(current_token)
                current_token = ''
        elif c == '(' or c == ')':
            if current_token:
                tokens.append(current_token)
                current_token = ''
            tokens.append(c)
        i += 1
    if current_token:
        tokens.append(current_token)
    return tokens
def get_precedence(operator):# Get the precedence level of an operator
    precedence = {
        '||': 1,
        '&&': 2,
        '==': 3,
        '!=': 3,
        '<': 4,
        '>': 4,
        '<=': 4,
        '>=': 4,
        '+': 5,
        '-': 5,
        '*': 6,
        '/': 6
    }
    return precedence.get(operator, -1)


def construct_syntax_tree(tokens):
    '''
    The construct_syntax_tree function takes a list of tokens
     as input and constructs a syntax tree for the given expression
    '''
    output_stack = [] # Stack to hold output nodes
    operator_stack = [] #Stack to hold operators

    for token in tokens:
        if token.isdigit():
            output_stack.append(Node(token))
        elif token in ('+', '-', '*', '/', '<', '>', '==', '!=', '&&', '||', '<=', '>='):
            while (len(operator_stack) > 0 and
                   operator_stack[-1] != '(' and
                   get_precedence(token) <= get_precedence(operator_stack[-1])):
                right_child = output_stack.pop()
                operator = operator_stack.pop()
                left_child = output_stack.pop()
                node = Node(operator, left_child, right_child)
                output_stack.append(node)
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                right_child = output_stack.pop()
                operator = operator_stack.pop()
                left_child = output_stack.pop()
                node = Node(operator, left_child, right_child)
                output_stack.append(node)
            if operator_stack and operator_stack[-1] == '(':
                operator_stack.pop()

    while len(operator_stack) > 0:
        right_child = output_stack.pop()
        operator = operator_stack.pop()
        left_child = output_stack.pop()
        node = Node(operator, left_child, right_child)
        output_stack.append(node)

    return output_stack[0]

def evaluate_expression(expression):
    tokens = tokenize(expression)
    syntax_tree = construct_syntax_tree(tokens)
    return syntax_tree.evaluate()

