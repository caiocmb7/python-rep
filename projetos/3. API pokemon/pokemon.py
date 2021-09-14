import requests

def foto_pokemon(nome_pokemon):
    resp = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}")
    dados = resp.json()
    print(f"A foto de frente do seu pokemon está nesse link: {dados['sprites']['front_shiny']}")
    print(f"A foto de costas do seu pokemon está nesse link: {dados['sprites']['back_shiny']}")

def onde_encontrar(nome_pokemon):
    resp2 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}")
    dados2 = resp2.json()
    print(f"Você pode encontrar o pokemon nesses locais: {dados2['location_area_encounters']}")

if __name__ == "__main__":
    foto_pokemon("pikachu")
    onde_encontrar("pikachu")