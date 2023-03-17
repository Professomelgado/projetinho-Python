from random import randint
computador = randint(0,10)
palpites = 0
print('SOU SEU COMPUTADOR,ACABEI DE PENSAR EM UM NUMERO... ')
acertou = False
while not acertou:
    jogador =int(input('QUAL NUMERO EU PENSEI?'))
    palpites += 1
    if jogador < computador:
        print('MAIS....tente denovo: ')
    if jogador > computador:
        print('MENOS...tente denovo: ')
    else:
        if jogador == computador:
            acertou = True
print('PARABENS, Voce acertou com {} palpites '.format(palpites))

