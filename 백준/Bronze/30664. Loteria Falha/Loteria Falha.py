while True:
    n = int(input())
    if not n:
        break
    if n % 42 == 0:
        print("PREMIADO")
    else:
        print("TENTE NOVAMENTE")
