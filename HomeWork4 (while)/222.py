n = int(input())

if 1 < n <= 1000:
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            print("*35*")
        elif i % 3 == 0:
            print("*3*")
        elif i % 5 == 0:
            print("*5*")
        else:
            print(i)
        i += 1