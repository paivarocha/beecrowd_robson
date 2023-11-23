#Ler nome funcionario (descartado)
nome = (input('Nome do funcionario:'))

#Ler Salario fixo 
salarioF = float(input('Salario fixo:'))

#Ler total de vendas 
vendasT = float(input('Valor de vendas no mes:'))
 
#15% das vendas + salarioF
comissao = (vendasT * 15) / 100
salarioTotal = comissao + salarioF

#PrintarT TOTAL
print(f'TOTAL = R$ {salarioTotal:.2f}')