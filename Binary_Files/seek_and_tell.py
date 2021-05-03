# f=open('random.txt','r')
# print(f.tell())
# f.seek(3)
# print(f.tell())
# print(f.read())
# f.seek(6)
# print(f.tell())
# print(f.read(8))
# print(f.tell())
# print(f.read())
# f.close()

'''
Description of seek()

f.seek(number,offset)
number - tells the number of characters to move forward
offset = 0 seeks from starting of file
offset = 1 seeks from the current position of the pointer
offset = 2 seeks from the end of the file
'''

f=open('random.txt','rb')
# print(f.tell())
# f.seek(5)
# print(f.tell())
# print(f.read(5))
# print(f.tell())
f.seek(5)
print(f.read(5))
f.seek(-8,2)
print(f.tell())
print(f.read())