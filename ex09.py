'Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada: '''

try: # 

    x = int(input('Digite um número inteiro: '))

except ValueError:

    print('ERRO! Digite um número inteiro válido.')
    exit() # encerra o programa!

print(f'A tabuada de {x} é: ')
count = 0
while count < 11:
    print(f'{x} x {count:>2} = {x * count}')
    count = count + 1

