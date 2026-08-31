numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))

operacao = input("Informe a operação (+, -, * ou /): ")

if operacao == "+":
    resultado = numero1 + numero2
    print("Resultado:", resultado)

elif operacao == "-":
    resultado = numero1 - numero2
    print("Resultado:", resultado)

elif operacao == "*":
    resultado = numero1 * numero2
    print("Resultado:", resultado)

elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print("Resultado:", resultado)
    else:
        print("Erro: não é possível dividir por zero.")

else:
    print("Erro: operação inválida.")
