#n = int(input())
#arr = []
#for _ in range(n):
#   arr.append(int(input()))
#A = int(input())
#B = int(input())
#maxi = []
#count = 0

#for i in range(n):
#    if arr[i] > 0:
#       count += 1
#        if i == 2:
#            arr[i] -= A
#        else:
#            arr[i] -= B
#    else:
#        pass
#maxi.append(count)
#print(min(maxi))

arr = []
count = 0
n = int(input())
for i in range(n):
    arr.append(int(input()))
A = int(input())
B = int(input())
maxi = max(A, B)
mini = min(A, B)
arr = sorted(arr)
while arr[n-1] > 0:
    count += 1
    arr[n-1] = arr[n-1] - maxi
    for j in range(n-1):
        arr[j] = arr[j] - mini
        arr = sorted(arr)
print(count)
