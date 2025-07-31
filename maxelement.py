import math

a = [110,20,30,40,48]
#max1
a.sort()
print("maximum element is :",a[-1])


#max2
print(max(a))

#max3
ma = a[0]
for i in range(len(a)):
    if a[i] > ma:
        ma = a[i]
print(ma)

#min1
a.sort()
print(a[0])

#min2
print(min(a))

#min3
min1 = math.inf
min2 = math.inf
for i in range(len(a)):
    if a[i] < min1:
        min1 = a[i]
print(min1)
for i in range(len(a)):
    if a[i] != min1 and a[i] < min2:
        min2 = a[i]

print(min2)

print(a[1])