from sqlalchemy import true

def reiniciar(): # criando uma função para reiniciar todo o script Obs: minha primeira função (:

    """Exercício Python 23: Faça um programa que leia um número de 0 a 9999
    e mostre na tela cada um dos dígitos separados.
    Obs utilizando listas, funçoes, loops e tratando erros inseridos pelo usuário"""


while true: # laço para tratamento de erro
    try: # enquanto a atribuição a variavel número não for inteiro 
        numero = int(input('Digite um número inteiro entre 0 a 9999: '))
        break # sai do loop de for um inteiro
    except ValueError: # trata o erro antes de reiniciar
        print('Ops! Você deve digitar um número!')

lista_numero = str(numero) # converte em string
lista_numero = lista_numero.replace('',' ') # atribui espaços a lista entre as string's >> números
lista_numero = lista_numero.split() # divide as casas da lista por espaços

if len(lista_numero) >= 5:  # verifica o tamanho da string e retorna erro se for maior ou igua a 5  
    x = str(input('Deseja reiniciar o programa? Se SIM digite [s] se NÃo digite [n]! ')) 
    if x == 's':
        reiniciar() 

    elif x == 'n':
        print('Programa encerrado!')
        exit(0)
    else:
        print('Escolha uma opção!')
        reiniciar()
# verifica o tamanho da lista e atribui os valores
elif len(lista_numero) == 4:
    print(f'A unidade é {lista_numero[3]}') 
    print(f'A Dezena é {lista_numero[2]}')
    print(f'A centena é {lista_numero[1]}')
    print(f'O milhar é {lista_numero[0]}')

elif len(lista_numero) == 3:
    print(f'A unidade é {lista_numero[2]}') 
    print(f'A Dezena é {lista_numero[1]}')
    print(f'A centena é {lista_numero[0]}')

elif len(lista_numero) == 2:
    print(f'A Dezena é {lista_numero[1]}')
    print(f'A centena é {lista_numero[0]}')
else:
    print(f'A Dezena é {lista_numero[0]}')
    

  
 
   