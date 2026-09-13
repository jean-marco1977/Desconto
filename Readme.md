# 💰 Desconto de Produtos sem registro

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub](https://img.shields.io/badge/github-8da0cb?style=for-the-badge&labelColor=555555&logo=github)

## 📝 Sobre o Projeto
Este é um script simples em **Python** desenvolvido para calcular o desconto de produtos de representação hipotética calculando apenas o valor gasto. 

O objetivo do sistema é auxiliar no calculo de desconto de uma loja, permitindo que o usuário identifique qual seria seu gasto e calculando o desconto final.

---

## 🧮 Fórmula Utilizada
O cálculo do valor gasto e do valor cobrado com desconto baseia-se nas seguintes fórmulas matemáticas implementadas no código:

1. **Desconto de até R$200:**
   \[\text{Valor Final} = {\text{Valor gasto} \times \text{Desconto (0.05)}}\]

2. **Desconto de 200 a R$300:**
   \[\text{Valor Final} = {\text{Valor gasto} \times \text{Desconto (0.10)}}\]

2. **Desconto de mais de R$300:**
   \[\text{Valor Final} = {\text{Valor gasto} \times \text{Desconto (0.15)}}\]

---

## 📂 Estrutura do Código
O programa foi construído com a seguinte lógica em Python (`App.py`):

```python
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
```

---

## 🚀 Como Executar o Programa

### Pré-requisitos
Antes de começar, você vai precisar ter o **Python 3.x** instalado em sua máquina.

### Passo a Passo

1. **Clone o repositório** (ou baixe o arquivo `Jean_Ag6_DS_I.py`):
   ```bash
   git clone https://github.com/jean-marco1977/Desconto/blob/main/Jean_Ag6_DS_I.py
   ```

2. **Navegue até a pasta** do projeto:
   ```bash
   cd nome-do-repositorio
   ```

3. **Execute o script** pelo terminal ou prompt de comando:
   ```bash
   python Jean_Ag6_DS_I.py
   ```

4. **Interaja com o terminal** inserindo o valor do que foi gasto.
