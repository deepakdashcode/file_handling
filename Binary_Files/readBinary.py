import pickle
def write():
    d={'TEZ':['Tushar','Dibya','Krishna'],'TEP':['Raju','Sohan','Rahul']}
    with open('bin1.txt','wb') as f:
        pickle.dump(d,f)
#write()

def read():
    with open('bin1.txt','rb') as f:
        dic=pickle.load(f)
    print(dic)

read()
