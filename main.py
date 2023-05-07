import pandas 
import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)

soup = BeautifulSoup(r.text ,"html.parser")

name = soup.find_all("a",class_="title")

names = [item.text for item in name ]
print(names)

price = soup.find_all("h4",class_="pull-right price")

prices = [p.text for p in price]
print(prices)

desc = soup.find_all("p",class_="description")
descs= [d.text for d in desc]
print(descs)

rev = soup.find_all("p",class_="pull-right")
revs = [r.text for r in rev]
print(revs)

df = pandas.DataFrame({"Product name":names, " Product Price": prices, " Reviews": revs})

df.to_csv("Productdetails.csv")


