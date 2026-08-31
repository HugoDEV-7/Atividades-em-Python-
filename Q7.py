nota = float(input("Digite a nota do aluno: "))

if nota >= 0 and nota < 5:
    print("Reprovado")
elif nota >= 5 and nota < 7:
    print("Recuperação")
else:
    print("Aprovado")
