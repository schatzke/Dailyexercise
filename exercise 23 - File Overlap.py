'''
Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any other number. And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. The explanation is easier with an example, which I will describe below.)

Discussion
You’ll need to stitch together a few ideas of things I’ve previously talked about on this blog, so if you need a refresher in any of these topics, now is your chance! Of course, there are any number of ways to do this exercise, so these are only suggestions.
'''
# Solution: loop
with open ('exercise 23 - happynumbers.txt','r') as list1:
	num_list1=list1.readlines()
with open ('exercise 23 - primenumbers.txt','r') as list2:
	num_list2=list2.readlines()
overlap_numlist=[]

for num in num_list1:
	if num in num_list2:
		overlap_numlist.append(int(num.replace('\n','')))	
# overlap_numlist = [ int(num.replace('\n',''))  for num in num_list1 if num in num_list2]		
print (overlap_numlist)

# Solution:function
def readlist(filename):
	list_of_ints=[]
	with open(filename,'r') as f:
		line = f.readline()
		while line:
			list_of_ints.append(int(line))
			line = f.readline()
	return list_of_ints
num_list1= readlist('exercise 23 - happynumbers.txt')
num_list2= readlist('exercise 23 - primenumbers.txt')
overlap_numlist = [ num for num in num_list1 if num in num_list2]
print (overlap_numlist)	



