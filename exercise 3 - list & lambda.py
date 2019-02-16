''' exercise 3:
    Take a list, say for example this one:

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    and write a program that prints out all the elements of the list that are less than 5.

    Extras:

    Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
    Write this in one line of Python.
    Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
'''

# Solution:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]
# code 1 use if
for i in a:
    if i<=5:
        b.append(i)
print (b)

# code 2 use lambda
b=list(filter(lambda x:(x<=5),a))
print (b)

# code 3 with lambda in one line
print (list(filter(lambda x:(x<=5),a)))

num=int(input('please enter a number:'))
print (list(filter(lambda x:(x<=num),a)))
