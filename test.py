import csv

# Data to be written to the CSV file
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 24, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 18, 'Chicago']
]

# Specify the name of the CSV file
filename = 'people.csv'

# Writing to the CSV file
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Writing each row
    for row in data:
        writer.writerow(row)

print(f"CSV file '{filename}' created successfully.")
