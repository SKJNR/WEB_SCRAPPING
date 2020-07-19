'''''IMPORTING LIBRARIES'''''
from selenium import webdriver
import os 
import shutil
import os
import requests
import pandas as pd
import csv

''''creating an instance of google chrome''''

DRIVER_PATH ='F:\data sets\chromedriver.exe.exe'

'''to run chrome in a headfull moe(like regular chrome)'''

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
my_page = driver.get("https://www.amazon.in/s?i=apparel&bbn=1968256031&rh=n%3A1571271031%2Cn%3A%211571272031%2Cn%3A1953602031%2Cn%3A1968253031%2Cn%3A1968256031&s=popularity-rank&lo=image&pf_rd_i=1968253031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=a9066e0f-f26e-4568-9230-26d6a7e1af78&pf_rd_r=6WGHRGE0JHCJHJJN0KXC&pf_rd_s=merchandised-search-5&ref=QANav11CTA_en_IN_1")


'''MAKE DIRECTORY TO SAVE IMAGES AND URLS'''

def make_directory(dirname):
    current_path = os.getcwd()
    path = os.path.join(current_path, dirname)
    if not os.path.exists(path):
        os.makedirs(path)

make_directory('sarees')


''''SCRAP THE URLS OF IMAGES ,BRANDS ,PRICES''''

product_data={}
product_data['brands']=[]
product_data['prices']=[]
product_data['ratings']=[]
product_data

''''SCRAPPING MULTIPLES PAGES AND STORE IT INTO CSV FORMAT''''

for page in range(current_page,end_page+1):
    images=driver.find_elements_by_xpath("//img[@class='s-image']")
    brands=driver.find_elements_by_xpath("//h5[@class='s-line-clamp-1']")
    prices=driver.find_elements_by_xpath("//span[@class='a-price']")
    ratings=driver.find_elements_by_xpath("//span[@class='a-icon-alt']")
    
    urls=[]
    for image in images:
        source=image.get_attribute('src')
        urls.append(source)
    
    for index,link in enumerate(urls):
        print("Downloading {0} of {1} images from page 1".format(index+1,len(urls)))
        response=requests.get(link)
        with open('saress/img_{0}{1}.jpeg'.format(index,page),"wb") as file:
            file.write(response.content)
    
    for brand in brands:
        product['brands'].append(brand.text)
    
    for price in prices:
        product['prices'].append(price.text)
    
    for rating in ratings:
        product['ratings'].append(rating.text)
    df=pd.DataFrame(product)
    df.to_csv('product.csv',encoding='utf-8-sig')

