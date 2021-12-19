import requests
from bs4 import BeautifulSoup
import pandas as pd

baseurl = "https://www.chewy.com/"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
productlinks = []
t={}
data=[]
c=0
for x in range(1,6):
    k = requests.get('https://www.chewy.com/castor-pollux-organix-organic-chicken/dp/158203'
    soup=BeautifulSoup(k,'html.parser')
    productlist = soup.find_all("li",{"class":"product-grid__item"})


    for product in productlist:
        link = product.find("a",{"class":"product-card"}).get('href')
        productlinks.append(baseurl + link)


for link in productlinks:
    f = requests.get(link,headers=headers).text
    hun=BeautifulSoup(f,'html.parser')

    try:
        price=hun.find("p",{"class":"product-action__price"}).text.replace('\n',"")
    except:
        price = None

    try:
        about=hun.find("div",{"class":"product-main__description"}).text.replace('\n',"")
    except:
        about=None

    try:
        rating = hun.find("div",{"class":"review-overview"}).text.replace('\n',"")
    except:
        rating=None

    try:
        name=hun.find("h1",{"class":"product-main__name"}).text.replace('\n',"")
    except:
        name=None

    try:
        name=hun.find("h1",{"class":"product-images"}).text.replace('\n',"")
    except:
        name=None

    try:
        name=hun.find("h1",{"class":"product-categories"}).text.replace('\n',"")
    except:
        name=None

    try:
        name=hun.find("h1",{"class":"product-key__benefits"}).text.replace('\n',"")
    except:
        name=None

    try:
        name=hun.find("h1",{"class":"product-brand"}).text.replace('\n',"")
    except:
        name=None

    try:
        name=hun.find("h1",{"class":"product-size"}).text.replace('\n',"")
    except:
        name=None

    try:
        name=hun.find("h1",{"class":"product-ingrediants"}).text.replace('\n',"")
    except:
        name=None

    Castor & Pollux ORGANIX Organic Chicken & Sweet Potato Recipe Grain-Free Dry Dog Food = {"name":name,"price":price,"rating":rating,"about":about}

    data.append(Castor & Pollux ORGANIX Organic Chicken & Sweet Potato Recipe Grain-Free Dry Dog Food)
    c=c+1
    print("completed",c)

df = pd.DataFrame(data)

print(df)