from random import randint

def linha(x):
    print('-='*x)

x = randint(0, 100) #gera um número interio aleatório de 0 a 100
tentativas = 0
numeros = []
chutes = []
maiorqX = []
menorqX = []

#Título
linha(10)
print('ACERTE O NÚMERO')
linha(10)

print('Pensei em um número X, tente adivinhar:')

while True:
    tentativas += 1
    print(f'TENTATIVA {tentativas}')
    print(f'Palpites anteriores: {chutes}')
    print(f'X é Maior que {menorqX}')
    print(f'X é Menor que {maiorqX}')

    valor = int(input(''))

    if valor == x:
        print('ACERTOU!!')
        print(f'n° tentativas:{tentativas}')
        break
    else:
        chutes.append(valor)
        #Pensa em um número para comparar
        n2 = randint(0, 100)
        if menorqX == [] and maiorqX == []:
            print('A')
            while True:
                if n2 in numeros or n2 == x:
                    n2 = randint(0, 100)
                else:
                    break
        elif menorqX != [] and maiorqX == []:
            while True:
                if n2 in numeros or n2 == x or n2 < max(menorqX):
                    n2 = randint(0, 100)
                else:
                    break
        elif menorqX == [] and maiorqX != []:
            while True:
                if n2 in numeros or n2 == x or n2 > min(maiorqX):
                    n2 = randint(0, 100)
                else:
                    break
        elif menorqX != [] and maiorqX != []:
            while True:
                if n2 in numeros or n2 == x or n2 < max(menorqX) or n2 > min(maiorqX):
                    n2 = randint(0, 100)
                else:
                    break

        numeros.append(n2)

        if x < n2:
            linha(20)
            print('DICA:')
            print(f'X é menor que {n2}!')
            linha(20)
            maiorqX.append(n2)
        else:
            linha(20)
            print('DICA')
            print(f'X é maior que {n2}')
            linha(20)
            menorqX.append(n2)



            



