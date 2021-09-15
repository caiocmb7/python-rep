import requests
from bs4 import BeautifulSoup as bs

url = "https://www.yelp.com.br/search?cflt=restaurants&find_loc=Fortaleza%20-%20CE&start=0"

resp = requests.get(url)

soup = bs(resp.content, 'html.parser')

report = soup.find_all(attrs={"class" : "css-1pxmz4g"})

for i in report:
    nome_restaurante = i.text
    print(nome_restaurante)

report2 = soup.find_all(attrs={"class" : "i-stars__09f24___sZu0"})

for j in report2:
    nota_restaurante = []
    nota_restaurante.append(j["aria-label"])
    print(nota_restaurante)


#for j in report2:
    #estrela_restaurante = j.find("aria-label").text
    #print(estrela_restaurante)
