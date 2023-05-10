#Exercicios com todos os operadores
x1 = float(input("Digite um número: "))
x2 = float(input("Digite outro número: "))
soma = x1 + x2
sub = x1 - x2
div = x1 / x2
mult = x1 * x2
divInt = x1 // x2
exp = x1 ** x2


print(f"A soma entre os{x1} e {x2} é: {soma}") 
# com tratamento da saída 'f' para 3 números após a vírgula
print(f'A divisão entre{x1} e {x2} é {div:.3}')
print(f'A multiplicação entre{x1} e {x2} é {mult:.3}')
print(f'A divisão inteira entre{x1} e {x2} é {div:.3} e seu subproduto é {divInt:.3}')
print(f'A exponênciação entre {x1} e {x2} é {exp:.3}')

""" Outros Exemplos"""

# Exemplo 2
# Alinhamento de strings

"""nome = input("Qual seu nome? ")
print(f'Olá {nome:20}!') # Escreveo nome em 20 espaços
print(f'Olá {nome:>20}!')# Alinha nome á Direita
print(f'Olá {nome:^20}!')# Centraliza"""
