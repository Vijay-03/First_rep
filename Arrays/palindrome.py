def reverse(num):
    return int(str(num)[::-1])


def is_palindrome(num):
    return num == reverse(num)


num = int(input("Enter input:"))
while True:
    num = num + reverse(num)
    if is_palindrome(num):
        print(num)
        break

# inputs
# 195
# 5
