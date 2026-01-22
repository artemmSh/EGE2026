for x in range(1, 8):
    num = int(f'{x}1{x}', 16) + int(f'{x}3{x}3', 8)
    if num in [2 ** i for i in range(1, 20)]:
        print(x)
