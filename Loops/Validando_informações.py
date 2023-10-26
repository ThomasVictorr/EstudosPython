pessoas = [] #Lista principal 
dados = [] #Lista para coletar os dados
cont = 0 #contador para dizer qual cadastro está sendo feito

while True:
    cont += 1
    print(f'CADASTRO {cont}')

    nome = str(input('Nome: '))
    while True:
        if len(nome) < 3:
            print('Nome inválido!')
            nome = str(input('Nome: '))
        else:
            dados.append(nome)
            break

    idade = int(input('Idade: '))
    while True:
        if idade < 0 or idade > 150:
            print('Idade inválida!')
            idade = int(input('Idade: '))
        else:
            dados.append(idade)
            break

    salario = float(input('Salário: '))
    while True:
        if salario < 0:
            print('Salário inválido!')
            salario = float(input('Salário: '))
        else:
            dados.append(salario)
            break
    
    sexo = str(input('Sexo[M/F]:')).upper()
    while True:
        if sexo != 'M' and sexo != 'F':
            print('Sexo inválido!')
            sexo = str(input('Sexo[M/F: ]')).upper()
        else:
            dados.append(sexo)
            break
    
    estadocivil = str(input('Estado Civil[s, c, v, d]: '))
    while True:
        if estadocivil != 's' and estadocivil != 'c' and estadocivil != 'v' and estadocivil != 'd': 
            print('estado civil inválido')  
            estadocivil = str(input('Estado Civil[s, c, v, d]: '))
        else:
            dados.append(estadocivil)
            break
    
    pessoas.append(dados[:]) #Adiciona os dados coletados para a lista principal!
    dados.clear()
    print('-' * 20)

    #Pergunta se o usuário deseja continuar fazendo cadastro
    print('Deseja continuar cadastrando?')
    print('1 - SIM')
    print('2 - NÃO')
    r = int(input(''))

    while True:
        if r != 1 and r != 2:
            print('Opção inválida!')
            r = int(input(''))
        else:
            break

    if r == 2:
        print('-' * 20)
        print('Pessoas cadastradas:')
        print(pessoas)
        break
    else:
        pass