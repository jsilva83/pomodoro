with open('my_file.txt') as my_file:
    contents = my_file.read()
    print(contents)

with open('my_file.txt', 'a') as my_file:
    my_file.write('\nThis is my family.')

with open('another_file.txt', 'w') as my_file:
    my_file.write('This is a new file created in the program.')

# Alternative way.
# file = open('my_file.txt')
# contents = file.read()
# print(contents)
# file.close()
