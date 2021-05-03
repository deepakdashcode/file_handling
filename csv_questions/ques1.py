import csv


def write():
    r = input('Sure to run?\n')
    if r[0] == 'y' or r[0] == 'Y':
        pass
    else:
        exit()

    with open('my_file.csv', 'w', newline='') as f:
        file_writer = csv.writer(f)
        file_writer.writerow(['Item_number', 'Item_name', 'Quantity', 'Price'])
        all_items = []
        while True:
            try:
                item_number = int(input('Enter the item_number\n'))
                item_name = input('Enter the item_name\n')
                quantity = int(input('Enter the quantity\n'))
                price = int(input('Enter the Price\n'))
                current_item = [item_number, item_name, quantity, price]
                all_items.append(current_item)
                r = input('Enter q to exit\n')
                if r[0] == 'q' or r[0] == 'Q':
                    break
                else:
                    continue

            except:
                print('Invalid Input')
                continue
        file_writer.writerows(all_items)


def search_by_item_number():
    item_num = input('Enter the item_number\n')
    found = False
    with open('my_file.csv', 'r') as f:
        file_reader = csv.reader(f)
        for i in file_reader:
            if i[0] == item_num:
                found = True
                print(i)
    if not found:
        print('Not found')

def search_by_price(min,max):
    f=open('my_file.csv','r')
    file_reader=csv.reader(f)
    no_of_items=0

    for i in file_reader:
        if i[3].isnumeric() and (int(i[3]) in range(min,max+1)):
            no_of_items+=1
            print(i)
    if no_of_items==0:
        print('No Item Found In given Range')


def search_by_price1(min, max):
    f = open('my_file.csv', 'r')
    file_reader = csv.reader(f)
    no_of_items = 0
    next(file_reader)

    for i in file_reader:

        if int(i[3]) in range(min, max + 1):
            no_of_items += 1
            print(i[1])
    if no_of_items == 0:
        print('No Item Found In given Range')


search_by_price1(20000,60000)
