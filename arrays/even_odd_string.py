string = input()
even, odd = [], []
c = len(string)
for ch in string:
    if ch.isdigit():
        if int(ch) % 2 == 0:
            even.append(ch)
        else:
            odd.append(ch)
    if ch.isalnum():
        c -= 1

begin, end = [], []
if c % 2 == 0:
    begin = even
    end = odd
else:
    begin = odd
    end = even

if len(begin) > len(end):
    for i in range(len(end)):
        print("{}{}".format(begin[i], end[i]), end='')
    for num in begin[len(end):]:
        print(num, end='')
else:
    for i in range(len(begin)):
        print("{}{}".format(begin[i], end[i]), end='')
    for num in end[len(begin):]:
        print(num, end='')

# inputs
# t9@a42&516
# 5u6@25g7#@
