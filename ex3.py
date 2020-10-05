nome = (input('Digite o nome do aluno:'))
nota1 = float(input('Digite a nota da primeira avaliação:'))
nota2 = float(input('Digite a nota da segunda avaliação:'))

media = nota1 + nota2
total = media/2
print (total)

if total < 7:
    print('Reprovado')
else:
    print('Aprovado')