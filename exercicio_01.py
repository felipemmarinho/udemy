nome = input('Digite o seu nome : ')
idade_digitada = int(input('digite a sua idade :'))

if(nome == '') or (idade_digitada == ''):
    print('Desculpa você deixou campos vaxios')
else:
    idade = int(idade_digitada)

    print(f'Seu nome é : {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f"{'seu nome contém espaço' if ' ' in nome else 'seu nome não contém espaço'}")
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é : {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')

    
