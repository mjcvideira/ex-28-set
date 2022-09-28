if __name__ == '__main__':
    continuar = 's'
    while continuar == 's':
        num1 = int(input('1º numero'))
        num2 = int(input('2º numero'))
        if num1 == num2:
            print(f'são iguais')
        elif num1 < num2:
            print(f'o segundo numero ({num2}) é maior que o primeiro ({num1})')
        else:
            print(f'o primeiro numero {num1} é maior que o segundo ({num2})')
        continuar = input('Repetir [s  n]? ')
