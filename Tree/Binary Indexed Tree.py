# Fenwick Tree or Binary Indexed Tree

def sum_query(bit,r):
    j=r+1
    result=bit[j]
    while j>0:
        j-=j&(-j)
        result+=bit[j]
    return result

# this function only updates the bit, not array
def update(bit,n,i,value):
    i+=1
    while i<n:
        bit[i]+=value
        i+=i&(-i)
    return bit

def createBIT(array):
    n=len(array)+1   # 0 node is dummy node, BIT starts from node 1
    bit=[0]*n
    for i in range(n-1):
        update(bit,n,i,array[i])
    return bit

array=[3,2,6,5,-3,3,8]
bit=createBIT(array)
print(bit)
print(sum_query(bit,3))

# find sum[l:r] -> sum(r)-sum(l-1)
lr = sum_query(bit,6)-sum_query(bit,3)
print(lr)

update(bit,7,4,1)
print(bit)
