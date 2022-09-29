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
    print(a)



