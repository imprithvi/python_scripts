'''
# This is one way of doing this
num1 = 1.5
num2 = 2.7
sum = float(num1) + float(num2)
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
'''

'''
# Now lets feed inputs to our script 

num1 = input("Please enter first number :")
num2 = input("Please enter second number :")
sum = float(num1) + float(num2)
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
'''


# Now this can be done in a single line 

print('The sum is %.1f' %(float(input('Enter first number: '))+float(input('Enter second number: '))))
