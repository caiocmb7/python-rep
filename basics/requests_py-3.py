import requests

def foto_pokemon(nome_pokemon):
    resp = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}")
    dados = resp.json()
    print(f"A foto do seu pokemon está nesse link: {dados['sprites']['front_shiny']}")

if __name__ == "__main__":
    foto_pokemon("pikachu")

