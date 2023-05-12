import math


print('Crie um algoritmo que leia um número, e mostre seu dobro, triplo e raiz quadrada')
x = int(input('Digite um número: '))
print(f'O dobro de {x} é {x*2}')
print(f'O triplo de {x} é {x*3}')
y = math.sqrt(x) #função raiz quadrada
print(f'A raiz quadrada de {x} é {x**(1/2)}')
print(f'>>Ou utilizando função<< A raiz qudrada de {x} é {y}')