#ler dois int tempo e velocidade
vm = int (input('digite a vm:'))
tempo = int (input('digite o tempo:'))

#formula distancia 
distancia = tempo * vm
print(distancia)

#consumo dos 12kml
consumo = distancia / 12

print (f'{consumo:.3f}')

