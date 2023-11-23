#ler 3 valores inteiros
a, b, c = input('digite os 3 valores').split()
a = int(a)
b = int(b)
c = int(c)

#formula maiorAB
maior = max(a, b, c)
print(f'{maior:.0f} eh o maior')
#print maior