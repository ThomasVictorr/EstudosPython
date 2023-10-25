n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))

maior = n1
menor = n1

#Teste do maior número
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

#Teste do menor número
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print('=-' * 10)
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')

