''' exercise 4：
    Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
    (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example,
    13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

# Solution:
num = int(input('please enter a integer:'))
if num ==0:
    print ('0 do not have divisor')
elif num==1:
    print([1])
else:
    print (list(filter(lambda x:num%x==0,range(1,num))))
