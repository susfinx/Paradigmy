def multi_tab(n):
    for i in range (1, n+1):
        for j in range(1, n+1):
            produkt = i * j
            print(f'{i}*{j} = {produkt}')
        print('----------')

n = int (input('Enter n: '))
multi_tab(n)
