#1 Basic Text File Operations
filename = 'sample_text.txt'
content = """Hello, World!
This is a sample text file.
It contains multiple lines or text for testing file operations"""

with open(filename, 'w') as file:
    file.write(content)
print(f"Content has been written to {filename}")


with open(filename, 'r') as file:
    read_content = file.read()

print("Content read from the file")
print(read_content)

#2 Processing CSV Files (writing and reading)

import csv

csv_filename = "people.csv"
data = [
    ["Name", "Age", "City"],
    ["Sultan", "19", "Bishkek"],
    ["Dan", "24", "Bishkek"],
    ["Bob", "35", "Los Angeles"]
]

with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
print(f'Data has been written to {csv_filename}')
print(f'Reading data from the CSV file:')
with open(csv_filename, 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

#3 Appearing Data to an Existing File

filename = 'sample_text.txt'
additional_text = "\nThis line is appended to file."

with open(filename, 'a') as file:
    file.write(additional_text)
print(f"Additional text has been appended to {filename}")

with open(filename, 'r') as file:
    updated_content = file.read()

print("Updated content on the file:")
print(updated_content)
