import math as mt
raio = float(input('Digite o raio do círculo: '))

if (raio != int) or (raio != float):
    print('Insira um valor numérico.')

area = (mt.pi*(raio)**2)
comprimento = (2*((mt.pi)*raio))    
print('O círculo de raio ','%.2f' %raio,'tem área igual a ','%.2f' %area,'e comprimento igual a ','%.2f' %comprimento)