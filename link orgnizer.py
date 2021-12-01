f = open ("raw url.txt","r+")
f2 = open('search url.txt', "w")

r = f.readlines()
list = []
str = ''
for i in r:
    if i[0] == 'h':
        list.append(i.strip())

        
print(list)
f.close()
f2.close()




