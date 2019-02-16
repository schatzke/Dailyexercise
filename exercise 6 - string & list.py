'''
exercise 6 - string & list
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''
# Solution 1
a=str(input('Please enter a str: '))
l=len(a)
x=0
for i in range(0,l):
	if a[i]!=a[l-1-i]:
		x=1
if x==0:
	print ('the str %s you enter is palindrome'%(a))
else:
	print ('the str %s you enter is not palindrome'%(a))
	
# Solution 2
b=str(input('Please enter a str: '))
b_reversed=a[::-1]
if b==b_reversed:
	print ('the str %s you enter is palindrome'%(b))
else:
	print ('the str %s you enter is not palindrome'%(b))
