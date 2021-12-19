from bs4 import BeautifulSoup
import numpy as np
from time import sleep
from random import randint
from selenium import webdriver

###########################
# Loop of all the pages
###########################

#Loop to go over all pages
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

