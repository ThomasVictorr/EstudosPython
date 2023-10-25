n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota no aluno: '))
m = (n1 + n2) / 2

if m >= 7 and m != 10:
    print('Aluno aprovado.')
elif m < 7:
    print('Aluno reprovado.')
elif m == 10:
    print('Aluno aprovado com Distinção.')
