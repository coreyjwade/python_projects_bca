'''
This is a hangman game for the user.
You need to import random_word
'''

from random_word import RandomWords



r = RandomWords()
word = r.get_random_word(hasDictionaryDef = 'true')
word = word.lower()
space = list(word)
dash = []
dash.extend(word)
#print(word)
for i in range(len(dash)):
	dash[i] = "_"

print(' '.join(dash))
print()

turns = 10 
already_guessed = []
while turns > 0:
	guess = input('If you think you know the word enter word. Other wise guess a letter: ')
	guess = guess.lower()
		

	if guess in space:
		for i in range(len(space)):
			if space[i] == guess:
				dash[i] = guess
		print('You got a letter right!')
	elif guess == "word":
		word_guess = input("\n What is the word? ")
		word_guess = word_guess.lower()
		if word_guess == word:
			print(f'You win! \n The word was {word}')
			break

	else:
		print("Wrong! \n")
		already_guessed.append(guess)
		print('You have wrongly guessed', already_guessed,'\n') 
		turns = turns - 1
		print(f'You have {turns} fails before you lose.')
			


	print(" ".join(dash))
	print()
print('You win!')
print(f'The word was {word}')

if turns == 0:
    print('You lose!')
    print(f'The word was {word}')

