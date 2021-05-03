import csv
def write():
    r = input('Sure to run?\n')
    if r[0] == 'y' or r[0] == 'Y':
        pass
    else:
        exit()
    with open('my_test.csv', 'w',newline='' ) as f:
        write_to_file = csv.writer(f)
        write_to_file.writerow(['Name', 'Class'])
        for i in range(2):
            name = input('Enter name\n')
            class_number = int(input('Enter the class\n'))
            ls = [name, class_number]
            write_to_file.writerow(ls)

def read():
    with open('my_test.csv', 'r') as f:
        reader_object=csv.reader(f)
        for i in reader_object:
            print(i)



write()
read()

