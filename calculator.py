import myfunctions

num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')
text = input('For addition press 1, for subtraction 2, for division 3 and for multiplication 4: ')

if(text == '1'):
    myfunctions.my_sum(num1,num2)
elif(text == '2'):
    myfunctions.subtract_Fun(num1,num2)
elif(text == '3'):
    myfunctions.div_Fun(num1,num2)
elif(text == '4'):
    myfunctions.multiply_Fun(num1,num2)