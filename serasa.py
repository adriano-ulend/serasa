import requests
from bs4 import BeautifulSoup as BS

login = {
    'login': 47454327,
    'password': '0Ulend2@'
}

def input_neg():

    url = 'https://sitenet.serasa.com.br/Logon/autentica'
    r = requests.get(url)
    if r.status_code != 200:
        raise ValueError('Unavailable url')
    else:
        return r.status_code


if __name__ == '__main__':
    print(input_neg())


# TO-DO TASKS:
# 01. procedimento de login atraves de requests/selenium (back)
# 02. ao acessar login, mapear com bs4 o html (buscar/selecionar tags)
# 03. leitura de dados de um arq externo, inputando em determinados campos (submit ao final)
# 04. verificar arq/protocolo de efetivação de negativação
# 05. avaliar a geracaoção

