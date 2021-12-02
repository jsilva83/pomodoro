# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Getting list of names from file.
input_file = open('./Input/Names/invited_names.txt', 'r')
names_list = input_file.readlines()
input_file.close()
for n in range(len(names_list)):
    names_list[n] = names_list[n].strip('\n')
# Replacing the names in each letter.
input_file = open('./Input/Letters/starting_letter.txt', 'r')
letter_content = input_file.read()
input_file.close()
letter_content = letter_content.replace('[name]', names_list[0])
pass
