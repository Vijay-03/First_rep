def is_palindrome(num1, num2):
    check = num1 + num2
    check = str(check)
    if check == check[::-1]:
        return check


inpnum = int(input())
res1 = []
res2 = []
num1 = 0
num2 = 0

while inpnum != 0:
    for i in range(0, inpnum):
        if str(i) == str(i)[::-1]:
            res1.append(i)

    for j in range(inpnum + 1, 10000):
        if str(j) == str(j)[::-1]:
            res2.append(j)

    num1 += max(res1)
    num2 += min(res2)

    if is_palindrome(num1, num2):
        print(is_palindrome(num1, num2))
        break
    else:
        inpnum -= 1
