import csv
def read():
    with open('file1.csv', 'r', newline='') as f:
        student_reader = csv.reader(f, delimiter=':')
        for i in student_reader:
            print(i)

read()