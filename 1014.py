#ler int distatncia e float combustivel
distancia = int(input('Digite a distancia percorrida:'))
combustivel = float(input('Digite a qtd de combustivel:'))

#calc media
consumo = distancia / combustivel

#print

print(f'{consumo:.3f} km/l')