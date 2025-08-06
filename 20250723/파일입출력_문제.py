
with open('wordlist.txt','r+') as f:
    readdata = f.read()

print(readdata)

mystrlist = readdata.split(' ')
print(mystrlist)
mylist_cnv = {}
for s in mystrlist:
    tmp = s.strip()
    if tmp in mylist_cnv:
        mylist_cnv[tmp] = mylist_cnv[tmp] + 1
    else:
        mylist_cnv[tmp] = 1
print(len(mylist_cnv))
print(mylist_cnv)