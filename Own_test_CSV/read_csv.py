import csv
with open('file2.csv','r',newline='\r\n') as f:
    file_reader=csv.reader(f)
    for i in file_reader:
        print(i)