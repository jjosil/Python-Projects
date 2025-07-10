import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
df = pd.DataFrame(data)
a_letter = False

phonetic_dict = {row.letter:row.code for (index,row) in df.iterrows()}

while not a_letter:
	user_word = input("Enter a word: ").upper()
	try:
		word_in_phonetic = [phonetic_dict[letter] for letter in user_word]
	except KeyError:
		print("Sorry, only letters in the alphabet allowed.")
	else:
		print(word_in_phonetic)
		a_letter = True