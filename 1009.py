#Ler numero de funcionario
numF = int(input('numero do funcionario:'))

#Ler Horas trabalhadas
hrsT = int (input('Horas trabalhadas:'))

#Ler valor/hora
valorHr = float(input('Valor da hora de trabalho:'))

#Calcular salario
salario = hrsT * valorHr

#printar salario
print(f'NUMBER = {numF:.0f}')
print(f'SALARY = U$ {salario:.2f}')