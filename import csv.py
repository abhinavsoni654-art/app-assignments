import csv

with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) 

    for row in reader:
        name = row[0]
        marks = [float(m) for m in row[1:]]
        average = sum(marks) / len(marks)
        print(f'{name}: {average:.2f}')
