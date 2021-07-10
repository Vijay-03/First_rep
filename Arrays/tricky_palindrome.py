def is_palindrome(num1, num2):
    check = num1 + num2
    check = str(check)
    if check == check[::-1]:
        return check


inpnum = int(input())
# res1 = []
num1 = 0
num2 = 0

while inpnum != 0:
    while True:
        temp1 = inpnum - 1
        if str(temp1) == str(temp1)[::-1]:
            num1 += temp1
            break
        else:
            inpnum -= 1

    while True:
        temp2 = inpnum + 1
        if str(temp2) == str(temp2)[::-1]:
            num2 += temp2
            break
        else:
            inpnum += 1

    if is_palindrome(num1, num2):
        print(is_palindrome(num1, num2))
        break
    else:
        inpnum -= 1
