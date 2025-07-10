#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

input_letters_path = f"./Input/Letters/starting_letter.txt"
input_names_path = f"./Input/Names/invited_names.txt"
output_path = f"./Output/ReadyToSend/"
PLACEHOLDER = "[name]"


with open(input_names_path) as invited_file:
	invited_list = invited_file.readlines()

for name in invited_list:
	with open(input_letters_path) as letter_file:
		letter = letter_file.read()
		letter_to_send = letter.replace(PLACEHOLDER, name.strip())

	with open(f"{output_path}/letter_for_{name.strip()}.txt", "w+") as output_files:
		output_files.write(letter_to_send)