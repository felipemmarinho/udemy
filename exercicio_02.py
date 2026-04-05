numero = input('digite um número : ')
try:
    numero = int(numero)
    if numero % 2 == 0:
        print(f'O número {numero} é par ')
    else:
        print(f'O número {numero} é impar ')   
except:
    print('É necessário digitar um número inteiro !')    
    