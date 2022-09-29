import random


def get_random(ini, fim):
    return random.randrange(ini, fim + 1)


if __name__ == '__main__':
    l1 = [0, 0, 0, 0, 0]
    e = [0, 0]
    for x in range(len(l1)):
        print(f'ola')
        l1[x] = get_random(1, 50)
        onum = get_random(1,50)
        if onum not in l1:
            l1 = onum
            break
            print(f'ola')
