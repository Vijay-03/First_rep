numbers = list(map(int, input().split(',')))

id5 = numbers.index(5)
id8 = numbers.index(8)

Num1 = sum(numbers[:id5] + numbers[id8 + 1:])
Num2 = 0

for i in numbers[id5:id8 + 1]:
    Num2 = Num2*10 + i

# print(Num1, Num2)
print(Num1+Num2)

# inputs
# 3,2,6,5,1,4,8,9
