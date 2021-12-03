# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Getting list of names from file.
with open('./Input/Names/invited_names.txt', 'r') as input_file:
    names_list = input_file.readlines()
list_size = len(names_list)
for n in range(list_size):
    names_list[n] = names_list[n].strip('\n')
# Getting the text of each letter.
input_file = open('./Input/Letters/starting_letter.txt', 'r')
letter_content = input_file.read()
input_file.close()
# Write the files to destination folder.
for n in range(list_size):
    with open(f'./Output/ReadyToSend/{names_list[n]}.txt', 'w') as output_file:
        a_content = letter_content.replace('[name]', names_list[n])
        output_file.write(a_content)

