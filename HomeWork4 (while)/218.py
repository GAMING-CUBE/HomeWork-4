n = int(input())
a = 0

while n > 0:
    n //= 10
    a += 1

print(a)
