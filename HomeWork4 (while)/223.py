while True:
    n = int(input())

    if not n:
        break

    if n < 10:
        continue
    elif n > 100:
        break
    else:
        print(n)