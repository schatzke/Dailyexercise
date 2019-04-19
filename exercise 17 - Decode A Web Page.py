'''
Exercise 17  Decode A Web Page
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

Discussion
Concepts for this week:

Libraries
requests
BeautifulSoup
'''

# Solution
import requests
from bs4 import BeautifulSoup

source=requests.get('https://www.nytimes.com/').text
soup=BeautifulSoup(source,'lxml')
#print(soup.prettify())

for article in soup.find_all('div',class_='css-1ez5fsm esl82me1'):
	print (article.text)
