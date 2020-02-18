numeros = [1,2,3,4,5,6,7,8,9,10]
par = []
impar = []

#import random

#for i in range(10):
    
    #numeros = random.randrange(1,10)
    #print(numeros)

for item in numeros:
    if item % 2 == 0:
        par.append(item)
    else:
        impar.append(item)
print(par)
print(impar)