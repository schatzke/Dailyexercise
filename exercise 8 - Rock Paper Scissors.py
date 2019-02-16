'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock
'''
print('Game Start')
player1_name = input('Please enter your name(player1):')
player2_name = input('Please enter your name(player2):')
	
def compare():
	player1_enter=str(input('%s, Please choose your decision: Rock, Scissors, or Paper? '%(player1_name)))
	player2_enter=str(input('%s, Please choose your decision: Rock, Scissors, or Paper? '%(player2_name)))
	if player1_enter in ['Rock','Scissors','Paper'] and player2_enter in ['Rock','Scissors','Paper']:
		print (player1_name+': '+player1_enter)
		print (player2_name+': '+player2_enter)
		if player1_enter == player2_enter:
			print ('Draw')
		elif player1_enter=='Rock':
			if player2_enter=='Scissors':
				print ('Congratulations! '+player1_name+', You win!')
			else:
				print ('Congratulations! '+player2_name+', You win!')
		elif player1_enter=='Scissors':
			if player2_enter=='Paper':
				print ('Congratulations! '+player1_name+', You win!')
			else:
				print ('Congratulations! '+player2_name+', You win!')
		elif player1_enter=='Paper':
			if player2_enter=='Rock':
				print ('Congratulations! '+player1_name+', You win!')
			else:
				print ('Congratulations! '+player2_name+', You win!')
	else:
		print ('Invalid enter, Please enter your decision again.')
		return compare()
	
compare()
while True:
	restart_game=input('Do you want to restart the game? enter Y or N:')
	if restart_game=='Y':
		print('Game restart')
		compare()
	else:
		print('Game Over')
		break
		
