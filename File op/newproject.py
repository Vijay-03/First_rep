samples, ranges =[int(i) for i in input().split()]
count = 0
final = []
arr = list(map(int, input().split()))
for i in range(0, ranges):
    range1, range2 = [int(i) for i in input().split()]
    for j in range(0, samples):
        if range1 <= arr[j] <= range2:
            count = count + 1
    final.append(count)
    count = 0
for i in range(0, len(final)):
    print(final[i], end=" ")