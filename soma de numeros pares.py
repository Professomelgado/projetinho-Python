soma = 0
cont = 0
for v in range(1,7):
    numero = int(input('DIGITE O {} VALOR: '.format(v)))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print('VOCE INFORMOU {} NUMEROS PAR, E A SOMA ENTRE ELES É DE {} '.format(cont,soma))