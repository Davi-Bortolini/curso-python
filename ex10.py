
'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e calcule quantos dólares
ela pode comprar'''

import json
import requests

requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL') #requisitando dados
cotacao = requisicao.json() # atribui os elementos do arquivo .json para cotacao(Tupla)

print('Data de hoje: ', cotacao['USD']['create_date'])
print('O dólar americano está valendo R$:', cotacao['USD']['bid'], ' Reais')

dolar = float(cotacao['USD']['bid'])

# tratando erro de entrada de dados digitada pelo usuário!
try:
    reais = float(input('Quanto dinheiro você tem na carteira? R$ '))

except ValueError:
    print('ERRO! Digite um valor numérico.')
    exit()

print(f'Com o valor R$:{reais} Reais você pode comprar USD:{reais / dolar:.3} dólares')

