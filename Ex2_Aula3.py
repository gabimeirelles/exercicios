dias = {1:'Domingo', 2:'Segunda', 3:'Terça', 4:'Quarta',5:'Quinta',6:'Sexta',7:'Sábado'}
num_dig = int((input('Digite um valor entre 1 e 7: ')))

if (num_dig>=1) and (num_dig<=7):
    print(dias[num_dig])
else:
    print('Valor correspondente não encontrado.')  







