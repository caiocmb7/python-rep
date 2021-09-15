import requests
from bs4 import BeautifulSoup as bs

url = "https://www.yelp.com.br/search?cflt=restaurants&find_loc=Fortaleza%20-%20CE&start=0"

resp = requests.get(url)

soup = bs(resp.content, 'html.parser')

report = soup.find_all(attrs={"class" : "css-1pxmz4g"})

dic = {"Restaurantes": [], "Notas": []}

#varre para encontrar o nome dos restaurantes
for i in report:
    word = i.text.replace(u'\xa0', ' ')
    dic["Restaurantes"].append(word)

report2 = soup.find_all(attrs={"class" : "i-stars__09f24___sZu0"})

#varre para encontrar a nota média do restaurante
for j in report2:
    dic["Notas"].append(j["aria-label"])

print(dic)

#for j in report2:
    #estrela_restaurante = j.find("aria-label").text
    #print(estrela_restaurante)
