while True:
    numero_1= input('Digite um número: ')
    numero_2= input('Digite outro número: ')
    operador= input('Digite o operador (+, -, *, /): ')

    try:
        num_1_float= float(numero_1)
        num_2_float= float(numero_2)
    except:
        print('Um ou ambos os números são inválidos')
        continue

    operadores_permitidos= '+-*/'

    if len(operador) > 1:
          print('Digite apenas um operador')
          continue

    if operador not in operadores_permitidos:
          print('Esse operador é inválido')
          continue
    

    if operador== '+':
            print(f'A soma dos números é {(num_1_float + num_2_float)}')
    elif operador== '-':
            print(f'A subtração dos números é {(num_1_float - num_2_float)}')
    elif operador== '*':
            print(f'A multiplicação dos números é {(num_1_float * num_2_float)}')
    elif operador == '/':
            print(f'A divisão dos números é {(num_1_float / num_2_float)}')

    sair= input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair:
        break

