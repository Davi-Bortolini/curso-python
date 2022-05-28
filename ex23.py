from sqlalchemy import true

entrar = 's' #laço tratamento de erro /excedeu o tamanho da lista
while entrar == 's':

    while true: # laço para tratamento de erro para aceitar somente números
        try: # enquanto a atribuição a variavel número não for inteiro 
            numero = int(input('Digite um número inteiro entre 0 a 9999: '))
            break # sai do loop de for um inteiro
        except ValueError: # trata o erro antes de reiniciar
            print('Ops! Você deve digitar um número!')

    lista_numero = str(numero) # converte em string e divide os elementos em lista.

    if len(lista_numero) >= 5:  # verifica o tamanho da string e retorna erro se for maior ou igua a 5  
        x = str(input('Ops! Digite um número entre 0 e 9999 \nDeseja reiniciar o programa? Se SIM digite [s] ou qualquer tecla para encerrar!')) 
        if x == 's': 
            print('recomeçando!')
        else:
            print('Programa encerrado!')
            exit(0)
        
   # verifica o tamanho da lista e atribui os valores
    elif len(lista_numero) == 4:
        print(f'A unidade é {lista_numero[3]}') 
        print(f'A Dezena é {lista_numero[2]}')
        print(f'A centena é {lista_numero[1]}')
        print(f'O milhar é {lista_numero[0]}')
        exit(0)
        

    elif len(lista_numero) == 3:
        print(f'A unidade é {lista_numero[2]}') 
        print(f'A Dezena é {lista_numero[1]}')
        print(f'A centena é {lista_numero[0]}')
        exit(0)

    elif len(lista_numero) == 2:
        print(f'A Dezena é {lista_numero[1]}')
        print(f'A centena é {lista_numero[0]}')
        exit(0)
    else:
        print(f'A Dezena é {lista_numero[0]}')
        exit(0)

    # próximo ex23 com caculo >>>


  
 
   