'hw_3.1'
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
math_operation = input('Enter math operation: ')
if math_operation == '/' and num2 == '0':
    print('Division by zero')
else:
    result = eval(f'{num1} {math_operation} {num2}')
    print(f'Result: {result}')