n = int(input())

result = 0

i = 1
while i <= n:
    result += i / (i + 1)
    i += 1

print(round(result, 2))
