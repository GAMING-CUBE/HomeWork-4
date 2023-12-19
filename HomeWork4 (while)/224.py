n = 0

while not (1 <= n <= 1000):
    n = int(input())

a = []

num = 1
while num <= n:
    if num % 7 == 0 and num % 5 == 0:
        a.append(num)
    num += 1

if a:
    print(a)
