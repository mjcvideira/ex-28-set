"""
Escreva um programa em Python que pede ao utilizador que lhe forneça
dois números (x e y) e que escreve o valor de (x + 3 * y) * (x - y).
O seu programa deve gerar uma interação como a seguinte:
Vou pedir-lhe dois numeros
Escreva o primeiro numero, x = 5
Escreva o segundo numero, y = 6
O valor de (x + 3 * y) * (x - y) e: -23
"""

x = int(input('diz um numaro'))
y = int(input('diz outro'))
conta = (x + 3 * y) * (x - y)
print(int(f' O valor de (x + 3 * y) * (x - y) é {conta}.'))