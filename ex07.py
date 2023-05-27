print("""Desenvolva um programa que leia as notas de um aluno, calcule sua média, 
mostre na tela e diga se o aluno foi aprovado ou não""")

x = 0
while (x == 0): #loop para determinar o número de notas
    notas = int(input('De quantas notas deseja realizar a média? (NO MÁXIMO 4 NOTAS)'))
    nome = input('Qual o nome do aluno? ')

    if (notas > 4 or notas < 2):
        print('Ops!! De 2 até 4 notas!')

    else:
        x = 1

if notas == 2:

    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))

    med = (n1 + n2) / 2
    print(f'A média do aluno {nome} é {med}!')

elif notas == 3:
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    n3 = float(input('Digite a terceira nora: '))

    med = (n1 + n2 + n3) / notas
    print(f'A média do aluno {nome} é {med}!')

else:
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    n3 = float(input('Digite a terceira nota: '))
    n4 = float(input('Digite a quarta nota: '))

    med = (n1 + n2 + n3 + n4) / notas
    print(f'A média do aluno {nome} é {med}!')

if med >= 6.0:
    print(f'O aluno {nome} foi aprovado!')

else:
    print(f'O aluno {nome} não alcançou média acima de 6.0 e não foi aprovado!')

