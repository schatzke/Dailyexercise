'''
exercise 12 - List Ends
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

Concepts to practice
Lists and properties of lists
List comprehensions (maybe)
Functions
'''
# Solution 1:
import random
list_A=random.sample(range(10),random.randint(2,8)) #generate a random list with random(2-8) numers
print ('original list is list_A: ', list_A) 
def get_end(givenlist):
	# one way to take the first and last elements of given list: 
	list_B=[givenlist[0],givenlist[len(givenlist)-1]] 
	return list_B
print ('new list is list_B: ', get_end(list_A))


# Solution 2:
def get_end2(givenlist):
	list_B=[]
	list_B.append(givenlist[0])
	list_B.append(givenlist[len(givenlist)-1]) 
	return list_B
print ('new list is list_B: ', get_end2(list_A))

# Solution 3:
def get_end3(givenlist):
    list_B = []
    first, *mid, last = givenlist
    list_B.append(first)
    list_B.append(last)
    print('new list is list_B: ', get_end2(list_A))
get_end3(list_A)
