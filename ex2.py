def comfor(n1, n2):
    soma = 0
    for x in range(0, (n2 - n1) + 1):
        soma += n1 + x
        print(soma)
    return soma


def comwhile(n1, n2):
    soma = 0
    x = 0
    while x < (n2 - n1) + 1:
        soma += n1 + x
        x += 1
    return soma
if __name__ == '__main__':
    n1 = int(input('1º numero'))
    n2 = int(input('2º numero'))
    if n2 <= n1:
        print(f'erro')
    else:
        pergunta = (input('[for | while]'))
        while pergunta == 'while':
            print(f'Resultado: {comwhile(n1,n2)}')
            break
        while pergunta == 'for':
            print(f'Resultado: {comfor(n1, n2)}')
            break