valor = float(input("Digite o valor da compra: R$ "))

if valor > 500:
    desconto = valor * 0.10
    valor_final = valor - desconto
    print(f"Desconto: R$ {desconto:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")
else:
    print("Não há desconto.")
    print(f"Valor final: R$ {valor:.2f}")
