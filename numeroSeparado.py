nome = str(input('Digite o seu nome completo: ')).strip()
print('Seu nome em maiúsculas é: ', nome.upper())
print('Seu nome em minusculas é: ', nome.lower())
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(" "),'letras'))
print('Seu primeiro nome tem: {} letras'.format(nome.find(' ')))