import random
from datetime import date

def username():
	print('Finding username...')
	y = date.today().year
	m = date.today().month
	d1 = date.today().weekday() + 1
	if d1 == 1:
        	d2 = 'Monday'
	elif d1 == 2:
		d2 = 'Tuesday'
	elif d1 == 3:
		d2 = 'Wednesday'
	elif d1 == 4:
		d2 = 'Thursday'
	elif d1 == 5:
		d2 = 'Friday'
	elif d1 == 6:
		d2 = 'Saturday'
	else:
		d2 = 'Sunday'
	user = 'The username is:\n'
	user += d2
	user += str(m)
	user += str(y)
	print('Done!')
	return user


def findWord():
	d1 = date.today().weekday()
	f = open('words.txt', 'r')
	listOfWords = f.read().splitlines()
	if d1 == 1 or d1 == 2 or d1 == 3:
		length = 6
	elif d1 == 4 or d1 == 5:
		length = 7
	else:
		length = 8
	print('Finding possible words...')
	possWords = []
	for i in range(0,len(listOfWords)):
		word = listOfWords[i]
		if len(word) == length:
			possWords.append(word)
	print('Done! ', len(possWords), ' possible words found!')
	return possWords

def capitalise(possWords):
	print('Capitalising words...')
	for i in range(0, len(possWords)):
		possWords[i] = possWords[i].title()
	print('Done!')
	return possWords

def digit(possWords):
	print('Adding a single Digit number...')
	results = []
	for i in range(0,len(possWords)):
		index = i
		for i in range(0,9):
			word = possWords[index] + str(i)
			results.append(word)
	print('Done!')
	return results

def add_char(results):
	print('Adding non-alphanumeric characters...')
	chars = ['!','@','£','$','%','&','*','#']
	final = []
	for i in range(0,len(results)):
		wordIndex = i
		for i in range(0,len(chars)):
			word = results[wordIndex] + chars[i]
			final.append(word)
	print('Done!')
	return final

def export(final, user):
	print('Writing to results.txt...')
	f = open('results.txt','w')
	f.write(str(user + '\n'))
	f.write('The possible passwords are:\n')
	for i in range(0,len(final)):
		toWrite = final[i] + '\n'
		f.write(str(toWrite))
	print('Done!')

def display(final, user):
	print('There are ', len(final), ' possible password.'
	userinput = input('Do you wish to display the results now?\n')
	userinput = userinput.upper()
	if userinput == 'YES':
		print(user)
		print('The possible passwords are:')
		for i in range(0,len(final)):
			print(final[i])

user = username()
possWords = findWord()
possWords = capitalise(possWords)
results = digit(possWords)
final = add_char(results)
export(final, user)
display(final, user)
