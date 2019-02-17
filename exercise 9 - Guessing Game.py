'''
erercise 9 - Guessing Game
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

# Solution
import random
print ('Guessing Game starts')
random_num = random.randint(1,9)
guess_count =0
game =''
while game!='exit':
	guess_num = int(input('Please enter the number you guess between 1 to 9: '))
	guess_count+=1
	if random_num==guess_num:
		print ('Congratulations! the number you guess is exactly right')
		game='exit'
	elif random_num<guess_num:
		print ('the number you guess is too high. Please choose continue guess or exit.')
		game=input('yes to continue, exit to stop th game: ')
	else:
		print ('the number you guess is too low. Please choose continue guess or exit.')
		game=input('yes to continue, exit to stop th game: ')