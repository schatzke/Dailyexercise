'''
    xercise1:
    Create a program that asks the user to enter their name and their age.
    Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''
# Solution:
name = input ('Please enter your name:')
age = int(input ('Please enter your age:'))
yearof100=2019+100-age
# print ('Hi, %s, You will be 100 years old in year %d'%(name, yearof100))
print ('Dear Mr/Ms ' + name + ', you will be 100 years old in ' + str(yearof100) + '\n' )
