a = [
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]
      ]
ilhas = ['ter', 'pic', 'gra','fai', 'stm']
tipos = ['gasolina', 'gasoleo']

if __name__ == '__main__':
    for x in range(2):
        for y in range(5):
            while True:
                try:
                    a[x][y] = int(input(f' insira vendas de {tipos[x]} para {ilhas[y]}'))
                    break
                except ValueError:
                    print(f'Insira 1 valor válido para vendas de {tipos[x]} para {ilhas[y]}')
    for x in range(len(a)):
        total = 0
        for y in range(len(a[x])):
            total += a[x][y]
        print(f'total de vendas para {tipos[x]} = {total}')
    z = 0
    for y in range(len(a)):
        z += 1
        total = 0
        for x in range(len(a)):
            total += a[x][y]
        print(f'total de vendas para {ilhas[y]} é {total}')
