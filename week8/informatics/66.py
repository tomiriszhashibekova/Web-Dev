x = int(input())
sum = 0
arr = list(map(int, input().split()))
for i in range(0, x):
    if arr[i] /1>arr[i-1]:
        sum +=1
print(sum)