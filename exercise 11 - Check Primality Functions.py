'''
Exercise 11 - Check Primality Functions
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.

Discussion
Concepts for this week:
Functions
Reusable functions
Default arguments
'''

# Solution
num=int(input('please enter a number: '))
def judge_prime (num):
	a=0
	if num==1:
		a=0
	elif num ==2:
		a=1
	else:
		for i in range (2,num):
			if num%i==0:
				a+=1
	if a ==0:
		print ('The number you enter '+str(num)+' is not prime.')
	else:
		print ('The number you enter '+str(num)+' is prime. And it has '+str(a)+' divisors.')
judge_prime (num)
	
	
	
