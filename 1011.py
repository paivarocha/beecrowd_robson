cod1, qtd1, valor1 = input().split()
cod2, qtd2, valor2 = input().split()

qtd1 = int(qtd1)
valor1 = float(valor1)
qtd2 = int(qtd2)
valor2 = float(valor2)

valorT = (qtd1 * valor1) + (qtd2 * valor2)

#printar VALOR A PAGAR
print(f'VALOR A PAGAR: R$ {valorT:.2f}')