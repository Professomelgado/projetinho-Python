sexo=str(input('Qual seu sexo:[M] ou [F] '))
while sexo not in 'MmFf':
    sexo=str(input('dados invalidos,informe novamente: [M] ou [F] '))
print('Sexo {} registrado com sucesso '.format(sexo))
