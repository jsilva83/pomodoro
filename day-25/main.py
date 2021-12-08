# with open('weather_data.csv') as input_file:  #
#     lines = input_file.readlines()  #
# output = []  #
# for a_line in lines:  #
#     output.append(a_line.strip('\n').split(','))  #
# print(output)  #

# import csv
#
# with open('weather_data.csv') as input_file:
#     data = csv.reader(input_file)
#     temperatures = []
#     for row in data:
#         if row[0] != 'day':
#             temperatures.append(int(row[1]))
#     print(temperatures)

# import pandas as pd
# import statistics
#
# data = pd.read_csv('weather_data.csv')
# print(data)
# print(data['temp'])
# data_dictionary = data.to_dict()
# print(data_dictionary)
# data_series = data['temp'].to_list()
# print(data_series)
# average = statistics.mean(data_series)
# print(round(average, 2))
# data_series = data['temp']
# average = data_series.mean()
# maximum = data_series.max()
# print(f'average = {average}, maximum = {maximum}')

# Which row as the max temperature.
# max_temp_row = data[data.temp == data.temp.max()]
# print(max_temp_row)

# Temperature of Monday in fahrenheit.
# fahr_temperature_monday = float(data[data.day == 'Monday'].temp) * 9 / 5 + 32
# print(f'Monday temperature in fahrenheit is: {fahr_temperature_monday}')

# Multiple conditions.
# rows = data[data.temp == data.temp.max() or data.temp == 12]
# print(rows)

# Create a dataframe from scratch.
# b_data_dictionary = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65],
# }
#
# b_data = pd.DataFrame(b_data_dictionary)
# b_data.to_csv('new_data.csv')
# print(b_data)

import pandas as pd

# Import the data series from CSV file but only a data series with the colors of squirrels.
a_data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv', usecols=['Primary Fur Color'])
# Create a series with only the unique values of color and counting.
counting_furs = a_data.value_counts(ascending=True)
# Initialize the dictionary to create the output dataframe set.
out_dictionary = dict(Fur_color=[], Count=[])
# Loop through the items of the data series and build the data dictionary.
for index, value in counting_furs.items():
    out_dictionary['Fur_color'].append(index[0])
    out_dictionary['Count'].append(value)
# Create the dataframe set from the dictionary of counting per unique color.
out_data = pd.DataFrame(out_dictionary)
# Output the CSV file.
out_data.to_csv('squirrel_count.csv')

# Second version based on course.
data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
grey_squirrel_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrel_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel_count = len(data[data['Primary Fur Color'] == 'Black'])
data_dict = {
    'Fur_color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}
df = pd.DataFrame(data_dict)
df.to_csv('squirrel_count(1).csv')
