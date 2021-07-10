def rotate(string, num):
    sum = 0
    while num > 0:
        sum += (num % 10)**2
        num = num // 10

    if sum % 2 == 0:
        print(string[-1] + string[:-1])   # right rotation
    else:
        print(string[2:] + string[:2])     # left rotation


s = input().split(',')
for i in s:
    string, num = i.split(':')
    num = int(num)
    rotate(string, num)



# inputs
# rhdt:246,ghftd:1246
