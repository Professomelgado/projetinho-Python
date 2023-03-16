n1 = int(input('PRIMEIRO VALOR: '))
n2 = int(input('SEGUNDO VALOR: '))
opçao = 0
while opçao != 5:
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] QUEM É MAIOR?
    [4] NOVOS NUMEROS
    [5] SAIR DO PROGRAMA''')
    opçao = int(input('QUAL SUA OPÇAO?'))
    if opçao == 1:
        soma = n1 + n2
        print('{} + {} = {} '.format(n1,n2,soma))
    elif opçao == 2:
        multi = n1 * n2 
        print('{} x {} = {} '.format(n1,n2,multi))
    elif opçao == 3:
        if n1 > n2:
            print('{} é maior que {} '.format(n1,n2))
        else:
            print('{} é maior que {} '.format(n2,n1))
    elif opçao == 4:
        print('INFORME OS NUMEROS NOVAMENTE: ')
        n1 = int(input('PRIMEIRO VALOR: '))
        N2 = int(input('SEGUNDO VALOR: '))
    elif opçao == 5:
        print('FINALIZANDO...')

    else:
        print('OPÇAO INVALIDA')
print('FIM DO PROGRAMA')
