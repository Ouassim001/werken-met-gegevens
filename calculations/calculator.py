
print('1. ADD')
print('2. SUBSTRACT')
print('3. MULTIPLY')
print('4. DIVIDE')
print('Select an operation to perform: ')
 
 operation = input()

 if operation == 1:
    num1 = input('enter first number: ')
    num2 = input('enter second number: ')
    print('the answer is ' + num1 + num2)
elif operation == 2:
     num1 = input('enter first number: ')
     num2 = input('enter second number: ')
    print('the answer is ' + num1 - num2)
elif operation == 3:
     num1 = input('enter first number: ')
     num2 = input('enter second number: ')
    print('the answer is ' + num1 * num2)
elif operation == 4:
     num1 = input('enter first number: ')
     num2 = input('enter second number: ')
     print('the answer is ' + num1 / num2)
else:
    print('invalid entry')