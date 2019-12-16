from math import ceil,log2
def build(node,start,end):
    if start==end:
        tree[node]=arr[start]
    else:
        mid=(start+end)//2
        build(2*node+1,start,mid)
        build(2*node+2,mid+1,end)
        tree[node]=tree[2*node+1]+tree[2*node+2]

def query(node,start,end,l,r):
    if r<start or end<l:
        return 0
    if l<=start and end<=r:
        return tree[node]
    mid=(start+end)//2
    return query(2*node+1,start,mid,l,r) + query(2*node+2,mid+1,end,l,r)

def update(node,start,end,x,val):
    if start==end:
        arr[x]+=val
        tree[node]+=val
    else:
        mid=(start+end)//2
        if start<=x<=mid:
            update(2*node+1,start,mid,x,val)
        else:
            update(2*node+2,mid+1,end,x,val)
        tree[node]=tree[2*node+1]+tree[2*node+2]
n=6
arr=[1,3,5,7,9,11]
tl=2*(2**ceil(log2(n)))-1
tree=[0]*tl
build(0,0,5)
print(tree)
print(query(0,0,5,1,3))
