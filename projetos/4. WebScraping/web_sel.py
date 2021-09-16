from selenium import webdriver
from time import sleep
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

driver = webdriver.Chrome()

url = "https://www.yelp.com.br/search?cflt=restaurants&find_loc=Fortaleza%20-%20CE&start=0"

resp = requests.get(url)

soup = bs(resp.content, 'html.parser')

# abrindo o navegador e clicando no botao "entrega em domicílio"
driver.get("https://www.yelp.com.br/search?cflt=restaurants&find_loc=Fortaleza%20-%20CE&start=0")
sleep(2)
botao_filtro = driver.find_element_by_xpath('/html/body/yelp-react-root/div[1]/div[4]/div/div[1]/div[1]/div[2]/div/ul/li[3]/div/div[2]/div[1]/div/button/span/div/div[1]')
botao_filtro.click()

# procurando quantas páginas (abas) existem para fazer a varredura em tudo
url2 = driver.current_url
resp = requests.get(url2)
soup = bs(resp.content, 'html.parser')
report3 = soup.find(attrs={"class" : "border-color--default__09f24__3Epto text-align--center__09f24__2qZj2"})
limite_pagina = report3.text[-2:]
print(limite_pagina)
# criando um dicionario onde irão ficar armazenados nossos dados colhidos
dic = {"Restaurantes": [], "Notas": []} 

# loop que irá acessar a página e todas as outras existentes, colhendo os dados delas
try:
    for i in range(int(limite_pagina)):
            new_url = driver.current_url
            resp = requests.get(new_url)
            soup = bs(resp.content, 'html.parser')

            #varre para encontrar o nome dos restaurantes
            report = soup.find_all(attrs={"class" : "css-1pxmz4g"})   
            for i in report:
                word = i.text.replace(u'\xa0', ' ')
                dic["Restaurantes"].append(word[4:])

            report2 = soup.find_all(attrs={"class" : "i-stars__09f24___sZu0"})

            #varre para encontrar a nota média do restaurante
            for j in report2:
                dic["Notas"].append(j["aria-label"][0:1])
            
            sleep(2)

            driver.execute_script("window.scrollTo(0, 2650)") 

            sleep(1)

            botao_proximo = driver.find_element_by_xpath('/html/body/yelp-react-root/div[1]/div[4]/div/div[1]/div[1]/div[2]/div/ul/li[14]/div/div[1]/div/div[11]/span/a/span')
            botao_proximo.click()

except:
    print("Erro")

finally:
    print(dic)



