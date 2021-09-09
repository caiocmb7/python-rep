import requests

resp = requests.get("https://viacep.com.br/ws/01001000/json/")

print(resp.text)
dados = resp.json() #para poder acessar ao dicionario
print(f"O cep é: {dados['cep']}")
print(f"O local desse cep {dados['cep']} é: {dados['localidade']}")
