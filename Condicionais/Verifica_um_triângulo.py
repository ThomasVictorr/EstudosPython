print('-='* 30)
print('Digite valores para Criar um triângulo')
n1 = int(input('Lado1: '))
n2 = int(input('Lado2: '))
n3 = int(input('Lado3: '))

#Verifica se é possível formar um triângulo com os valores informados:
if n1 + n2 > n3 and n1 + n3 > n2 and n3 + n2 > n1:
    #Verifica qual o tipo do triângulo:
    if n1 == n2 == n3:
        print('Com os valores informados foi gerado um triângulo EQUILATERO.')
    elif n1 != n2 != n3:
        print('Com os valores informados foi gerado um triângulo ESCALENO.')
    elif n1 == n2 or n1 == n3 or n3 == n2:
        print('Com os valores informados foi gerado um triângulo ISOSCELES.')
else:
    print('Com os valores informados não é possível criar um triângulo.')
