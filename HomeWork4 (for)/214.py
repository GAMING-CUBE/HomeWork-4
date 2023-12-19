normal = 0
negative = 0
zero = 0

number = int(input())

for i in range(number):
    num = int(input())

    if num > 0:
        normal += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print(f"{normal} {negative} {zero}")