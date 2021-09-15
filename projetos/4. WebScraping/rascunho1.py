import requests
from bs4 import BeautifulSoup as bs

def avaliacao():
    url_base = "https://br.trustpilot.com/review/"

    url_review = input("Digite uma url válida do site para a revisão no 'trustpilot': ")

    url_analise = url_base + url_review

    resp = requests.get(url_analise)

    soup = bs(resp.content, 'html.parser')

    for escolha in soup.find_all("article", attrs={"class" : "review"}):
        comentario = escolha.img['alt']
        print(comentario)



avaliacao()


