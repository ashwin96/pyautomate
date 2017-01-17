import bs4,requests
url = raw_input("enter the url: ")
r = requests.get(url)
r.raise_for_status()
data = r.text
val = bs4.BeautifulSoup(data,"html.parser")
for data in val.find_all('div',class_="a-link-normal a-color-tertiary"):
	print "Product type:" + data.get_text()
for data in val.find_all(class_="a-size-large",id="productTitle"):
	print data.get_text()
for data in val.find_all("span",id="priceblock_saleprice",class_="a-size-medium a-color-price"):
        print data.get_text()
   
