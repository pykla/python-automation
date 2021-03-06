import os
import csv
import json
# ADAH Adah adah AdaH  ADAH => Adah
csv_name = input('Please provide the name for your CSV: ')

file_path = 'csv/' + csv_name + '.csv' # csv/bolaji.csv

if not os.path.exists(file_path):
    print('The CSV doesnt exist. Ensure the CSV exists in the csv folder of the project')
else:
    print('The CSV exists.')
    search_name = input('What name would you like to search for? ').capitalize() # boy => Boy
    csv_file = csv.DictReader(open(file_path, 'r'))
    json_list = []
    for row in csv_file: # [json_list.append(row) for row in csv_file]
        json_list.append(row)

    data = [value for value in json_list if value.get(csv_name) == search_name]

    if data:
        print(data[0].get(csv_name) + ' exists')
    else:
        print('Data doesn\'t exist')
