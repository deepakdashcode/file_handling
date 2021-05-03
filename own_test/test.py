import pickle
f=open('test.dat','rb')
while True:
    try:
        ls=pickle.load(f)
        print(ls)
    except EOFError:
        break


