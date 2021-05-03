import sys

# sys.stdout.write('Enter first number\n')
# a=int(sys.stdin.readline())
#
# sys.stdout.write('Enter second number\n')
# b=int(sys.stdin.readline())
#
# if b==0:
#     sys.stderr.write("Can't divide any number by zero")
# else:
#     c=a/b
#     sys.stdout.write(str(c))
#


# sys.stdout.write('Enter the name of the file\n')
# file=sys.stdin.readline()
# f=open(file.strip(),'r')
# while True:
#     ch=f.read(1)
#     print(f'ch is {ch}')
#     if len(ch)==0:
#         sys.stderr.write('Reached the end of file\n')
#         break
#     else:
#         print(ch,end='')
# f.close()
f = open('test.txt', 'r')

while True:
    ch = f.read(1)
    if ch == '':
        sys.stderr.write('End\n')
        # print('End')
        break
    else:
        print(ch, end='')
