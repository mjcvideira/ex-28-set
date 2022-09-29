if __name__ == '__main__':
    vendas = [
          [10, 20 , 30, 40 , 50],
          [15, 25, 35, 45, 55]
      ]
    print(vendas)

    for venda in vendas:
        print(f' boas {venda}venda')
        for v in venda:
            print(f' lo{v}')
    x = 0
    y = 0

    total = 0
    for x in range(2):
        totall = 0
        for y in range(5):
            #print(f'x={x} y ={y} = {vendas[x][y]}')
            total = total + vendas[x][y]
            totall = totall + vendas[x][y]
        print(f'totalxxxxxxxxxx {total}')
    print(f'yyyyyyyyyyy {totall}')
    for x in range(len(vendas)):
        for y in range(len(vendas[0])):
            print(f'x={x} y ={y} = {vendas[x][y]}')
