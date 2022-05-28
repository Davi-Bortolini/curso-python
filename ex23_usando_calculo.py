from sqlalchemy import true

while true: # repete todo o script (erro de numero acima de 9999)

    while true: # laço para tratamento de erro para aceitar somente números
        try: # enquanto a atribuição a variavel número não for inteiro 
            numero = int(input('Digite um número inteiro entre 0 a 9999: '))
            break # sai do loop de for um inteiro
        except ValueError: # trata o erro antes de reiniciar
            print('Ops! Você deve digitar um número!')

    if numero >= 9999:  # verifica o tamanho da string e retorna erro se for maior ou igua a 5  
        x = str(input('Ops! Digite um número entre 0 e 9999 \nDeseja reiniciar o programa? Se SIM digite [s] ou qualquer tecla para encerrar!')) 
        if x == 's': 
            print('recomeçando!')
            
        else:
            print('Programa encerrado!')
            break

        #RESOLUÇAO USANDO MATEMÁTICA
    else:    
        unidade = numero // 1 % 10
        dezena = numero // 10 % 10
        centena = numero // 100 % 10
        milhar = numero // 1000 % 10

        print(f'A unidade é {unidade}') 
        print(f'A Dezena é {dezena}')
        print(f'A centena é {centena}')
        print(f'O milhar é {milhar}')
        exit(0)