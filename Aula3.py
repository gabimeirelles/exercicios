'''import random as rd 

contador = 1
lista = []

while (contador <= 20):
    lista.append(rd.randrange(0,1000))
    contador+=1
    
print("Essa é a lista:",lista)
print("O maior valor da lista é:",(max(lista)))
print("O menor valor da lista é:",(min(lista)))'''

'''import math as mt
import statistics as st 

print(mt.cos(45))
print(mt.pi)'''

'''dias = {1:'Domingo', 2:'Segunda', 3:'Terça', 4:'Quarta',5:'Quinta',6:'Sexta',7:'Sábado'}
num_dig = int((input('Digite um valor entre 1 e 7: ')))

if (num_dig>=1) and (num_dig<=7):
    print(dias[num_dig])
else:
    print('Valor correspondente não encontrado.')'''     

'''import random

num_itens = int(input('Digite o número de itens que deseja na lista: '))    
contador = 0
lista = []

while (contador<=num_itens):
    lista.append(random.randrange(0, 1000))
    contador+=1
print('A lista aleatória é: ',lista)
print('O maior valor é: ',max(lista))
print('O menor valor é: ',min(lista))'''

import math as mt
raio = float(input('Digite o raio do círculo: '))

if (raio != int) or (raio != float):
    print('Insira um valor numérico.')

area = (mt.pi*(raio)**2)
comprimento = (2*((mt.pi)*raio))    
print('O círculo de raio ','%.2f' %raio,'tem área igual a ','%.2f' %area,'e comprimento igual a ','%.2f' %comprimento)



