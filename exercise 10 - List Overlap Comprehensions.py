'''
exercise 10 - List Overlap Comprehensions 
This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.

Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python.

Extra:

Randomly generate two lists, and combine two lists without duplicates
'''

#Solution:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print ([i for i in set(a) if i in b])

import random
c=random.sample(range(100),random.randint(0,9))  #generate a random list with random(0-9) numers 
d=random.sample(range(100),random.randint(0,9))
print (c)
print (d)
print (list(set(c+d)))
