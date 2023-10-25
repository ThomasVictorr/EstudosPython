usuario = senha = str

usuario = str(input('Digite seu nome de usuário: '))

while True:
    senha = str(input('Digite sua senha:'))
    confirmaSenha = str(input('Confirme sua senha: '))
    if senha == confirmaSenha:
        print('-='*20) 
        print('Login realizado.')
        break
    else:
        print('As senhas não conferem!!!')

