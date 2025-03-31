5# print("PAVAN")


# a="panduga"
# print(a)

# n = int(input("give n value: "))
# i = 1

# while i<= n :
#     print(i)
#     i+=1

# for i in range(1,n):
#     print(i)
def list(a):
    count={}
    for el in a:
        if el in count:
            count[el]+=1
        else:
            count[el]=1
    return count.items()
a=[1,2,2,3,1,3,4]
print(list(a))

print([1])