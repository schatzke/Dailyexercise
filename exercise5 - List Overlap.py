''' 
	exercise 5：
	Take two lists, say for example these two:
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

	Extras:
	Randomly generate two lists to test this
	Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
'''

# Solution:
# Randomly generate two lists with 8 numbers
import random
'''
a=[]
b=[]
for i in range(0,6):
	x=random.randint(1,10)
	y=random.randint(1,10)
	a.append(x)
	b.append(y)
	
'''
# another way to Randomly generate two lists
a=random.sample(range(1,10),6)
b=random.sample(range(1,10),6)

print (a)
print (b)
# return a list that contains only the elements that are common between list a and b
c=[]
for i in a:
    if i in b and i not in c:
        c.append (i)
print (c)
