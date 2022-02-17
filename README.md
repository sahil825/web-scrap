# web-scrap
test

in chwe.py i have installed python library name Beautifulsoup which is used for web scraping purposes to pull the data out of html and xml files. it creates a parse tree from page source code that can be used to extract data in hierahical and more readable manner
the i have imported numpy as np which works as the fudamental packages for scientific computing in python 
i have also imported sleep which is used for to suspends execution for the given number of second. the arugment may be a floating point number to indicate a more precise sleep time 
i have also imported radint from random this function is used for to generates a new #random number everytime it executes 
the in have imported selenium it is an automation testing tool. it can create automation testing scripts which perform tests.
from bs4 import BeautifulSoup
import numpy as np
from time import sleep
from random import randint
from selenium import webdriver

this part of code is for importing some used python library which help for to do some extra work as i explai above 
then in next part which is 
pages = np.arange(1)
data=[]

for page in pages:
    
    page="https://www.chewy.com/b/food-332"
    driver = webdriver.Chrome()
    driver.get(page)  
    sleep(randint(2,10))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    my_table = soup.find_all(class_=['description', 'price-label body-3','price title-5',\
                                    'score orange big'])

    for tag in my_table:
        data.append(tag.get_text())

pages = np.arange(1, 3, 1)
url_collected=[]

is for to get in loop for checking which page product is on 

then next part which is 
for page in pages:
    page="https://www.chewy.com/b/food-332"
    page="https://www.chewy.com/b/wet-food-11730" 
    driver = webdriver.Chrome()
    driver.get(page)  
    sleep(randint(5,15))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    urls = [item.get("href") for item in soup.find_all("a")]
    
    
#Remove duplicates and none values
urls_final = list(dict.fromkeys(url_collected))
urls_final = list(filter(None, urls_final)) 

#Remove if not starting with pwa, remove if ending with display=reviews
url_final = [x for x in urls_final if x.startswith('/pwa/')]
url_final = [x for x in url_final if not x.endswith('display=reviews')]
   
string = 'https://www.chewy.com/'
final_list=[string + s for s in url_final]

data=[]

for i in range(0,10):
    url = final_list[i]
    driver2 = webdriver.Chrome()
    driver2.get(url)  
    sleep(randint(10,20))
    soup = BeautifulSoup(driver2.page_source, 'html.parser')
    my_table2 = soup.find_all(class_=['title-2', 'rating-score body-3'])
    
    review=soup.find_all(class_='reviews')[-1]
    
    try:
        price=soup.find_all('span', attrs={'class':'price'})[-1] 
    except:
        price=soup.find_all('span', attrs={'class':'price'})

    for tag in my_table2:
        data.append(tag.text.strip())
        
    for p in price:
        data.append(p)
        
    for r in review:
        data.append(r)  
        
 this is for to get an page number and show the price of each product which you have click in base url form as in url counter 
 
 
 as this is one the next code i have writen in new file decs.py the first part is same as chwe.py which is importing libraries in code 
 
 then next code block or part which is 
 baseurl = "https://www.chewy.com/"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
productlinks = []
t={}
data=[]
is  for adding base url to show which product description price and all requirement file you need in folowed code 
and headers part is to get which web browser you get get access to it

then next code block is 
for x in range(1,6):
    k = requests.get('https://www.chewy.com/castor-pollux-organix-organic-chicken/dp/158203'
    soup=BeautifulSoup(k,'html.parser')
    productlist = soup.find_all("li",{"class":"product-grid__item"})


    for product in productlist:
        link = product.find("a",{"class":"product-card"}).get('href')
        productlinks.append(baseurl + link)
which is for creating a for lop for which item you need to get detail in url form 

the nect code block which is 
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
this is bacialy the code which is used for showing or displayed the following or given atributes in url form and then last by calling the prin(df) funcion it will give the output in print form in output section and if run on websit it will display over url section 

And most important how to set up project and what are some other funcation are described in detail.txt file 
