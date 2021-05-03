import pickle

def get_all_records():
    records=[]
    with open('marks','rb') as f:
        while True:
            try:
                records.extend(pickle.load(f))
            except EOFError:
                break
    return records

def accept_marks():
    records = []
    with open('marks', 'wb') as f:
        while True:
            name = input('Enter your name\n')
            marks = int(input('Enter your marks\n'))
            current_student = [name, marks]
            records.append(current_student)
            ch = input('Enter q to exit\n')
            if ch == 'q':
                break

        pickle.dump(records, f)


# accept_marks()
#
# def read_content1():
#     # with open('marks','rb') as f:
#     #     records=pickle.load(f)
#     # #print(records)
#     # for i in records:
#     #     for j in i:
#     #         print(j,end='\t')
#     #     print()
#     #
#     #


def read_content():
    with open('marks', 'rb') as f:
        while True:
            try:
                s = pickle.load(f)
                for i in s:
                    print(i)
            except EOFError:
                break


def append_data():
    records = []
    with open('marks', 'ab') as f:
        while True:
            name = input('Enter your name\n')
            marks = int(input('Enter your marks\n'))
            current_student = [name, marks]
            records.append(current_student)
            ch = input('Enter q to exit\n')
            if ch == 'q':
                break

        pickle.dump(records, f)

def search_record():
    records=get_all_records()

    name=input('Enter the name of the student\n')
    found=False
    for i in records:
        if name==i[0]:
            print('Found!!!')
            found=True
            print(i)
    if not found:
        print('Not found')


# accept_marks()
# read_content()
# append_data()
def update_data():
    records=get_all_records()
    found=False
    name=input('Enter the name\n')
    for i in range(0,len(records)):
        if records[i][0]==name:
            found=True
            marks=int(input(f'Enter new marks for {name}\n'))
            records[i][1]=marks
            print('Marks changed successfully')
    if not found:
        print('No data found')

    with open('new_record.dat','wb') as f:
        pickle.dump(records,f)

def get_new_record():
    with open('new_record.dat','rb') as f:
        record=pickle.load(f)
    print(record)

def update_to_single():
    with open('new_record.dat','rb+') as f:
        records=pickle.load(f)
        name=input('Enter the name\n')
        found=False
        for i in range(0,len(records)):
            if records[i][0]==name:
                print(f'Enter the new marks of {name}')
                marks=int(input())
                records[i][1]=marks
                found=True
        if not found:
            print('Not found')
        else:
            f.seek(0) # Very Very important
            pickle.dump(records,f)




get_new_record()