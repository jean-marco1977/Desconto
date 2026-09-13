# Declaração de variaveis para o projeto do consumo de energia

valor_compra = float(input("Digite o valor da compra: "))

# Estrutura da funcionalidade do código e resposta do programa

if valor_compra < 200:
    desconto = valor_compra * 0.05
    valor_final = valor_compra - desconto
    print(f"\nO valor da compra é R${valor_compra:.2f}.")
    print(f"O desconto aplicado foi de R${desconto:.2f}.")
    print(f"O valor final da compra é R${valor_final:.2f}.")
elif valor_compra >= 200 and valor_compra < 300:
    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto
    print(f"\nO valor da compra é R${valor_compra:.2f}.")
    print(f"O desconto aplicado foi de R${desconto:.2f}.")
    print(f"O valor final da compra é R${valor_final:.2f}.")
else:
    desconto = valor_compra * 0.15
    valor_final = valor_compra - desconto
    print(f"\nO valor da compra é R${valor_compra:.2f}.")
    print(f"O desconto aplicado foi de R${desconto:.2f}.")
    print(f"O valor final da compra é R${valor_final:.2f}.")