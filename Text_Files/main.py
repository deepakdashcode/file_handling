f=open('test.txt')
s=' '
totalSize=0
reducedSize=0
while s:
    s=f.readline()
    totalSize+=len(s)
    reducedSize+=len(s.strip())

print('Total size =',totalSize)
print('Reduces Size =',reducedSize)
f.close()
