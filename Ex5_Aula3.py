import random

num_itens = int(input('Digite o número de itens que deseja na lista: '))    
contador = 0
lista = []

while (contador<=num_itens):
    lista.append(random.randrange(0, 1000))
    contador+=1
print('A lista aleatória é: ',lista)
print('O maior valor é: ',max(lista))
print('O menor valor é: ',min(lista))