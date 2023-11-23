import math
# Ler x1 e y1
x1, y1 = input().split()
x1 = float (x1)
y1 = float (y1)

#Ler x2 e y2
x2, y2 = input().split()
x2 = float (x2)
y2 = float (y2)

#Fazer formula
distancia = math.sqrt(((x2 - x1) **2) + ((y2 - y1) ** 2))

#print
print(f'{distancia:.4f}')