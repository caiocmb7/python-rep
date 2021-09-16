import requests
from bs4 import BeautifulSoup as bs

url = "https://www.yelp.com.br/search?cflt=restaurants&find_loc=Fortaleza%20-%20CE&attrs=RestaurantsDelivery&start=90"

resp = requests.get(url)

soup = bs(resp.content, 'html.parser')

# dic para amazenar os dados do webscraping
dic = {"Restaurantes": [], "Notas": [("null") for i in range(10)]} 
print(dic)
report = soup.find_all(attrs={"class" : "css-1pxmz4g"})
#varre para encontrar o nome dos restaurantes
for i in report:
    word = i.text.replace(u'\xa0', ' ') #estava aparecendo "\xa0" na string, esse método elimina tal fato.
    dic["Restaurantes"].append(word[4:])

report2 = soup.find_all(attrs={"class" : "i-stars__09f24___sZu0"})
report3 = soup.find_all(attrs={"class" : "priceCategory__09f24__Ylk7h"})


#varre para encontrar a nota média do restaurante

for j in report2:
    dic.update(j["aria-label"])
      
    
print(dic)
   


