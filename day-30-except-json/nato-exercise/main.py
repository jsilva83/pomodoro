# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas


def generate_nato_phonetic_word():
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
    # Create a dictionary in this format:
    phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
    print(phonetic_dict)
    # Create a list of the phonetic code words from a word that the user inputs.
    word = input("Enter a word: ").upper()
    # Check if a letter in not in phonetic_dict.
    for a_letter in word:
        try:
            a_value = phonetic_dict[a_letter]
        except KeyError:
            print(f'The key - {a_letter} - does not exist.')
    # Check if a letter in not in phonetic_dict - alternative 2.
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print(f'Invalid word "{word}".')
        # If invalid call the function again.
        generate_nato_phonetic_word()
    else:
        print(output_list)
    return


# Generate NATO word.
generate_nato_phonetic_word()
