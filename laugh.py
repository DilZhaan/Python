import requests
import json

import sys
sys.path.insert(0,'bs4.zip')
from bs4 import BeautifulSoup

#Imitate the Mozilla browser.
user_agent = {'User-agent': 'Mozilla/5.0'}


def compare_prices(product_laughs,product_glomark):
    #TODO: Aquire the web pages which contain product Price
    laughs_req = requests.get(product_laughs, headers = user_agent)
    glomark_req = requests.get(product_glomark)
    
    
    #TODO: LaughsSuper supermarket website provides the price in a span text.
    laughs_soup = BeautifulSoup(laughs_req.content, 'html.parser')
    price_laughs = float(laughs_soup.find('span' ,{"class":"regular-price"}).text.strip()[3:])
    product_name_laughs = laughs_soup.find("div",{"class":"product-name"}).text.strip()
    
    #TODO: Glomark supermarket website provides the data in jason format in an inline script.
    #You can use the json module to extract only the price
    glomark_soup = BeautifulSoup(glomark_req.content,'html.parser')
    data_glomark =json.loads(glomark_soup.find("script",{"type":"application/ld+json"}).text.strip())
    price_glomark = float(data_glomark['offers'][0]['price'])
    product_name_glomark = data_glomark['name']
   
    #TODO: Parse the values as floats, and print them.
    #price_laughs = float(laughs_soup.find("span ",{"class":"regular-price"}).text.strip()[3:1])
    
    
    print('Laughs  ',product_name_laughs,'Rs.: ' , price_laughs)
    print('Glomark ',product_name_glomark,'Rs.: ' , price_glomark)
    
    if(price_laughs>price_glomark):
        print('Glomark is cheaper Rs.:',price_laughs - price_glomark)
    elif(price_laughs<price_glomark):
        print('Laughs is cheaper Rs.:',price_glomark - price_laughs)    
    else:
        print('Price is the same')

laughs_tissues = 'https://scrape-sm1.github.io/site1/FLORA%20FACIAL%20TISSUES%202%20X%20160%20BOX%20-%20HOUSEHOLD%20-%20Categories%20market1super.com.html'
glomark_tissues = 'https://glomark.lk/flora-facial-tissues-160s/p/10470'
compare_prices(laughs_tissues,glomark_tissues)

laughs_bread = 'https://scrape-sm1.github.io/site1/Crimson%20Bread%20Sliced%20market1super.com.html'
glomark_bread = 'https://glomark.lk/sandwich-bread-450g/p/13606'
compare_prices(laughs_bread,glomark_bread)