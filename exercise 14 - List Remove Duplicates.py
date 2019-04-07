'''
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''
# Solution1 - using loop:
def list_remove_duplicates1 (alist):
	for i in alist:
		newlist=[]
		if i not in newlist:
			newlist.append(i)
	return newlist
alist=[4,7,9,3,5,8,3,6,5]
print ('the original list is:'+ str(alist))
print ('the new list is:'+ str(list_remove_duplicates1 (alist)))
		
# Solution2 - using set:
def list_remove_duplicates2 (alist):
	return list(set(alist))
alist=[4,7,9,3,5,8,3,6,5]
print ('the original list is:'+ str(alist))
print ('the new list is:'+ str(list_remove_duplicates2 (alist))) 
