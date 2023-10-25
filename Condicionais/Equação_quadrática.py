from math import sqrt

print('-='*22)
print('Digite os termos de uma EQUAÇÃO QUADRÁTICA:')

a = int(input('a: '))

#Se a = 0 o programa encerra
if a == 0:
    print('Não existe equação de segundo grau pois a = 0')

#se a > 0 o programa continua
else:
    b = int(input('b: '))
    c = int(input('c: '))

    delta = b**2 - 4 * a * c

    if delta < 0:
        print('Não há raízes reais para equação.')
    elif delta == 0:
        print('A equação possui apenas uma raíz real: ')
        print((-b + sqrt(delta)) / 2 * a)
    else:
        print('A equação possui duas raízes reais: ')
        print(f'raíz 1: {(-b + sqrt(delta)) / 2 * a}')
        print(f'raíz 2: {(-b - sqrt(delta)) / 2 * a}')