from bs4 import *
import requests as rq
import searchurl
links = []

for i in searchurl.L:
    r2= rq.get(i)
    soup2 = BeautifulSoup(r2.text, "html.parser")
    x = soup2.select('img[src]')
    for img in x:
        links.append(img['src'])
        print("one round over")

f= open('gif2.txt', "a")
f.write(str(links))
f.close()