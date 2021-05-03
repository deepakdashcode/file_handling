def read_content():
    f=open('test.txt', 'r')
    while True:
        s=f.readline()
        if s=='':
            break
        else:
            print(s,end='')

#read_content()
def read_1():
    n=0
    f=open(r'../newDir/text.txt', 'r')
    while True:
        s=f.readline()
        if s=='':
            break
        else:
            if s[0].lower()=='f' or s[0].lower()=='a':
                print(s,end='')
                n+=1
    print(n)

def BIGLINES():
    f = open(r'../newDir/text.txt', 'r')
    ls=f.readlines()
    for i in ls:
        if len(i)>50:
            print(i)

#BIGLINES()

def count_words():
    f = open(r'../newDir/text.txt', 'r')
    words=f.read().split()
    print(words)
    print(f'Number of words = {len(words)}')
    love_count=(words.count('love'))
    print(f'Number of occurrences of love are {love_count}')
    big_words=0
    is_up_to=0
    for i in words:
        if i=='is' or i=='up' or i=='to':
            is_up_to+=1

        if len(i)>5:
            big_words+=1
    print(f'Number of big words are {big_words}')
    print(f'Number of ISUPTO = {is_up_to}')

count_words()