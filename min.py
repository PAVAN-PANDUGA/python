array = list(map(int,input().split()))

def minimum(arr):
    mini=float('inf')
    for i in range(len(arr)):
        if arr[i]<mini:
            mini=arr[i]

    return mini
print(minimum(array))
