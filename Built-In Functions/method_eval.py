def evaluate_expression(s, num1=2, num2=5):
    """
    Evaluate an expression (Python statement or a code object)
    """
    return eval(s)

# Tests
print(evaluate_expression("2 + 2"))  # 4
print(evaluate_expression("num1 + num2"))  # 7
print(evaluate_expression("num1 + 1"))  # 3
print(evaluate_expression("num1"))  # 2
print(evaluate_expression("abs(num1)"))  # 2
print(evaluate_expression('input("Enter something: ")'))
