n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))

maior = n1
meio = n1
menor = n1

#Teste do maior número
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

#Teste do número do meio
if n2 > n1 and n2 < n3:
    meio = n2
if n3 > n1 and n3 and n3 < n2:
    meio = n3

#Teste do menor número
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print('=-' * 10)
print(f'Os números digitados em ordem decrescente são: {maior}, {meio} e {menor}')