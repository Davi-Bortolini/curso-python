from itertools import count


print("""Crie um prograna que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas a letras minúsculas
Quantas letras ao todo sem considerar espaços
quantas letras tem o primeiro nome""".upper())

nome = str(input('Digite seu nome completo: ')).strip() #elimina espaços antes e depois adicionados pelo usuário.
print('O nome digitado foi: ',nome)
print('O nome com todas as letras maiúsculas é: ',nome.upper()) # conv em maiúscula
print('O nome com todas as letras minúsculas é: ',nome.lower()) # conv em minúscula
print('A quantidade de letras no nome sem os espaços é: {}'.format(len(nome) - nome.count(' '))) # tamanho da string menos count(espaços)
print(f' Quantidade de letras no nome semos espaços é: {len(nome) - nome.count(" ")}') # mesmo metodo acima, porém na versao python 3.10.4 obs: aspas simples dentro dos colchetes gerava erro
print('A quantidade de letras no primeiro nome são: ',nome.find(' ')) # conta quantas letras até o primeiro espaço
print('''abaixo método alternativo que utilizei antes da resouçao do exercicio'''.upper())
nome2 = nome.split() # divide a string por espaços e atribui a outra variável
nome = nome.replace(' ', '') # a string nome foi redefinida definitivamente para sem espaços
print('A quantidade de letras sem considerar os espaços é: ',len(nome)) # conta o número de letras na varável nome modificada
print('A quantidade de letras no primeiro nome é de: ',len(nome2[0])) # conta as letras na posição 0 da lista.

