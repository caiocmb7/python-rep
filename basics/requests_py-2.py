import requests

def cep(valor_cep):
    resp = requests.get(f"https://viacep.com.br/ws/{valor_cep}/json/")
    print(f"As informações gerais do CEP digitado é: \n{resp.text}")
    dados = resp.json()
    print(f"O bairro desse CEP digitado é: {dados['bairro']}")

if __name__ == '__main__':
    cep(60150015)
