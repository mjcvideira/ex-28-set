if __name__ == '__main__':
    a = [
          [10, 20 , 30, 40 , 50],
          [15, 25, 35, 45, 55]
      ]
    total = 0
    for x in range(5):
        for y in range(2):
            total = a[0][y] + a[1][y]
            print(f' x={x}, y={y}')