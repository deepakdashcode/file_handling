import csv
f=open('file2.csv','w',newline='\r\n')
student_writer=csv.writer(f)
student_writer.writerow(['Roll','Name','Marks'])
records=[]
while True:
    try:
        print('Enter Roll , Name and Marks respectively')
        rno, name, marks = int(input()), input(), int(input())
        current_student = [rno, name, marks]
        records.append(current_student)
        print('Press q to exit')
        ch = input()
    except:
        print('Invalid input try again')
        continue
        pass



    if ch=='q' or ch=='Q':
        break
    else:
        continue

# Method 1
# for i in records:
#     student_writer.writerow(i)

# Method 2
student_writer.writerows(records)

f.close()
