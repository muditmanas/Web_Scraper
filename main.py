from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

import requests

# url = input("Enter a website to extract the URL's from: ")

r  = requests.get("https://www.medicalsparx.com/")

data = r.text

SOUP = soup(data)
dict1={}
i=0
for link in SOUP.find_all('a'):
    dict1[i]=link.get('href')
    i=i+1
    
    #####
    
my_url = 'https://www.medicalsparx.com/all-brands.html'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("li",{"class":"product product--tile"})
print(len(containers))

# print(soup.prettify(containers[0]))

container = containers[0]
print(container.img["alt"])

price = container.findAll("div",{"class":"product__price"})
print(price[0].text)

dict2={}

for container in containers:
    Product_Name = container.img['alt']
    price_container = container.findAll("div",{"class":"product__price"})
    Price = price_container[0].text.strip()
    
    # print(Product_Name,"-------->",Price)
    dict2[Product_Name]=Price


###################################


my_url = 'https://www.medicalsparx.com/dermal-fillers.html'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("li",{"class":"product product--tile"})
print(len(containers))

# print(soup.prettify(containers[0]))

container = containers[0]
print(container.img["alt"]) 

price = container.findAll("div",{"class":"product__price"})
print(price[0].text)

dict3={}

for container in containers:
    Product_Name = container.img['alt']
    price_container = container.findAll("div",{"class":"product__price"})
    Price = price_container[0].text.strip()
    
    # print(Product_Name,"-------->",Price)
    dict3[Product_Name]=Price


##########################


my_url = 'https://www.medicalsparx.com/aqualyx.html'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("div",{"class":"product-section"})
print(len(containers))

# print(soup.prettify(containers[0]))

container = containers[0]
print(container.img["alt"]) 
print(container.img["src"]) 


price = container.findAll("div",{"class":"productPrice price-per-unit product-82385"})
print(price[0].text)

pro_properties = container.findAll("div",{"class":"productProperties"})
print(pro_properties[0].text)
pro_properties = pro_properties[0].text

li=pro_properties.split('\n')
li[3]=li[3]+' '+li[4]


containers_information = page_soup.findAll("div",{"class":"article__textContainer"})
print(len(containers_information))
print(soup.prettify(containers_information[0]))
information = containers_information[0].text
li1=information.split('\n')


# dict4={}

# for container in containers:
#     Product_Name = container.img['alt']
#     price_container = container.findAll("div",{"class":"product__price"})
#     Price = price_container[0].text.strip()
    
#     # print(Product_Name,"-------->",Price)
#     dict4[Product_Name]=Price





