import requests
from bs4 import BeautifulSoup
urls=[]
paragraphs=[]
word_count={}
search=input("Enter Google Search URL:")
x=requests.get(search)
soup=BeautifulSoup(x.text,"html.parser")
for result in soup.find_all("a"):
    if "/url" in str(result):
        if "id=" not in str(result):
            if "class=" in str(result):
                if "%" not in result.attrs.get("href"):
                    urls.append(result.attrs.get("href"))
for i in range(len(urls)):
    urls[i]=urls[i].split("&",1)[0]
    urls[i]=urls[i].replace("/url?q=","")
for url in urls:
    x=requests.get(url,allow_redirects=False)
    soup=BeautifulSoup(x.text,"html.parser")
    for text in soup.find_all("p"):
        paragraphs.append(text.text)
paragraphs=" ".join(paragraphs)
words=paragraphs.split(" ")
for i in words:
    if i not in word_count:
        word_count[i]=1
    else:
        word_count[i]=word_count[i]+1
for i in sorted(word_count.items(), key=lambda item:item[1],reverse=True):
    print(str(i[0])+":"+str(i[1]))


