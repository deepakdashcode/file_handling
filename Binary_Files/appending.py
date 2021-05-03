import pickle


def write():
    records = []
    try:
        with open('student_data.dat', 'rb') as f:
            records = pickle.load(f)
    except:
        pass
    with open('student_data.dat', 'wb') as f:
        while True:
            name = input('Enter your name\n')
            marks = int(input('Enter your marks\n'))
            current_student = [name, marks]
            records.append(current_student)
            ch = input('Enter q to exit\n')
            if ch == 'q':
                break

        pickle.dump(records, f)


def read_content():
    with open('student_data.dat', 'rb') as f:
        records = pickle.load(f)
    for i in records:
        for j in i:
            print(j, end='\t')
        print()

def get_new_record():
    with open('new_record.dat','rb') as f:
        record=pickle.load(f)
    print(record)


read_content()
get_new_record()
