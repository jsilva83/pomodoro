# ✂︎ Section 1 -------------------------------- ︎✂︎
try:
    a_file = open('a_file.txt')
    a_dictionary = {'key': 10}
    print(a_dictionary['other_key'])
except FileNotFoundError:
    a_file = open('a_file.txt', 'w')
    a_file.write('Something')
except KeyError as error_message:
    print(f'That dictionary key - {error_message} - does not exist!')
else:
    a_file_content = a_file.read()
    print(a_file_content)
finally:
    a_file.close()
    print('File closed')

# ✂︎ Section 2 -------------------------------- ︎✂︎
a_height = float(input('Height: '))
# Raise an error.
if a_height > 2.5:
    raise ValueError('Human height should not be over 2.5 meters.2.')
a_weight = float(input('Weight: '))
a_bmi = a_weight / a_height ** 2
print(a_bmi)
