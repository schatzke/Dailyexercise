'''
Exercise 16 - Password Generator
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''

#Solution:
import random
import string

x=string.ascii_letters  # x='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
y=string.digits   # y='0123456789'
z=string.punctuation  # z='!#$%&()*+,-./:;<=>?@[\]^_`{|}~'

pswd_len=int(input('How many numbers you want to generate for your password? '))
pswd_select=str(input('Please tell you want weak password or strong. print W for weak, S for strong. ')) 

def generate_pswd (pswd_len,pswd_select):
	# if want weak password, generate a password with only letters, else mix with letters and numbers and punctuation
	if pswd_select =='W':
		return ''.join(random.sample(x,pswd_len))
		# return ''.join(random.choice(x) for _ in range(pswd_len))
	else:
		return ''.join(random.sample((x+y+z),pswd_len))

password = generate_pswd(pswd_len,pswd_select)
print (password)
