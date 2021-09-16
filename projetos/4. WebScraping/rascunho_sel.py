from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("https://www.yelp.com.br/search?cflt=restaurants&find_loc=Fortaleza%20-%20CE&start=0")

sleep(2)

botao_filtro = driver.find_element_by_xpath('/html/body/yelp-react-root/div[1]/div[4]/div/div[1]/div[1]/div[2]/div/ul/li[3]/div/div[2]/div[1]/div/button/span/div/div[1]')
botao_filtro.click()

sleep(2)

driver.execute_script("window.scrollTo(0, 2650)") 

sleep(1)

botao_proximo = driver.find_element_by_xpath('/html/body/yelp-react-root/div[1]/div[4]/div/div[1]/div[1]/div[2]/div/ul/li[14]/div/div[1]/div/div[11]/span/a/span')
botao_proximo.click()

sleep(2)

driver.back()

sleep(2)