string = input()
numbers = []
for dig in string:
    if dig.isdigit() and int(dig) not in numbers:
        numbers.append(int(dig))
numbers.sort(reverse=True)
id1 = -1
n = len(numbers)
for i in range(n-1, 0, -1):
    if numbers[i] % 2 == 0:
        id1 = i
        break
if id1 == -1:
    print(id1)
else:
    num = 0
    for i in range(n):
        if i == id1:
            continue
        else:
            num = num*10 + numbers[i]
    num = num*10 + numbers[id1]
    print(num)

# inputs
# infosys@337
# Hello#81@21349
