'hw_3.1'
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
math_operation = input('Enter math operation: ')
if math_operation == '/' and int(num2) == 0:
    print('Division by zero')
else:
    if math_operation == '+':
        result = int(num1) + int(num2)
    elif math_operation == '-':
        result = int(num1) - int(num2)
    elif math_operation == '*':
        result = int(num1) * int(num2)
    elif math_operation == '/':
        result = float(num1) / float(num2)
    else:
        result = 'Invalid operation'
    print(f'Result: {result}')