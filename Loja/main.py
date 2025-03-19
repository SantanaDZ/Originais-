import requests 
import json 

link = 'https://loja-e6ce2-default-rtdb.firebaseio.com/'

'''dados = {
    'produto': 'teclado',
    'preco': 150,
    'quantidade':'10' 
}
requisicao = requests.post(f'{link}Produtos/.json', data=json.dumps(dados))
print(requisicao)
print(requisicao.text)'''


dados = {'preco':1450}
req = requests.patch(f'{link}/Produtos/-OJz6_NqZLcIzujonA0I',data=json.dumps(dados))
print(req)
print(req.text)