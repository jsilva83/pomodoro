# Read files and initialize lists.
with open('file1.txt') as file1_obj:
    file1_numbers = file1_obj.readlines()
with open('file2.txt') as file2_obj:
    file2_numbers = file2_obj.readlines()
file1_numbers = [int(item.strip('\n')) for item in file1_numbers]
file2_numbers = [int(item.strip('\n')) for item in file2_numbers]
result = [item for item in file1_numbers if item in file2_numbers]
# Convert str figures to int.
# Write your code above 👆
print(result)
