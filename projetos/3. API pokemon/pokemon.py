import requests

def foto_pokemon(nome_pokemon):
    resp = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}")
    dados = resp.json()
    print(f"A foto de frente do seu pokemon está nesse link: {dados['sprites']['front_shiny']}")
    print(f"A foto de costas do seu pokemon está nesse link: {dados['sprites']['back_shiny']}")

def ataques_pokemon(nome_pokemon):
    resp2 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}")
    dados2 = resp2.json()
    for i in range(len(dados2['moves'])):
        print(f"Ataques do {nome_pokemon}: {dados2['moves'][i]['move']['name']}")
        
if __name__ == "__main__":
    foto_pokemon("ditto")
    ataques_pokemon("squirtle")