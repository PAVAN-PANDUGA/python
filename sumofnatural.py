# num = 8
# sum = 0
# for i in range(sum, num+1):
#     sum+=i
# print("sum of given natural number is :" , sum)


# num = 12
# print( num*(num+1)//2)



def recursum(n):
    if n == 0:
        return n
    return n + recursum(n-1)
n,sum = 8,0
print(sum(n))

