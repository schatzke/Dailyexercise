'''
Exercise 15 (and Solution)
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
'''

# Solution 1 -one line:
def reverseWord(w):
  return ' '.join(w.split()[::-1])
  
astr=str(input('Please enter a long str containing multiple words: '))
print (reverseWord(astr))

# Solution 2 - split
def reverse_v2(x):
  y = x.split()
  return " ".join(y[::-1])
print (reverse_v2(astr)) 

# Solution 3 - reversed
def reverse_v3(x):
  y = x.split()
  return " ".join(reversed(y))
print (reverse_v3(astr))
  
# Solution 4 - loop
def reverse_v4(x):
	y = x.split()
	result = []
	for word in y:
		result.insert(0,word)
	return " ".join(result)
print (reverse_v4(astr))
