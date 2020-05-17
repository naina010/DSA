from math import ceil,log2
def build(node,start,end):
    if start==end:
        tree[node]=arr[start]
    else:
        mid=(start+end)//2
        build(2*node+1,start,mid)
        build(2*node+2,mid+1,end)
        tree[node]=tree[2*node+1]+tree[2*node+2]

def lazy_query(node,start,end,l,r):
    if lazy[node]!=0:
        tree[node]+=(end-start+1)*lazy[node]
        if start!=end:
            lazy[2*node+1]+=lazy[node]
            lazy[2*node+2]+=lazy[node]
        lazy[node]=0
    if r<start or end<l:
        return 0
    if l<=start and end<=r:
        return tree[node]
    mid=(start+end)//2
    return lazy_query(2*node+1,start,mid,l,r) + lazy_query(2*node+2,mid+1,end,l,r)

def lazy_update(node,start,end,us,ue,val):
    if lazy[node]!=0:
        tree[node]+=(end-start+1)*lazy[node]
        if start!=end:
            lazy[2 * node + 1] += lazy[node]
            lazy[2 * node + 2] += lazy[node]
        lazy[node]=0
    if start>ue or us>end:
        return
    if us<=start and end<=ue:
        tree[node]+=(end-start+1)*val
        if start!=end:
            lazy[2*node+1]+=val
            lazy[2*node+2]+=val
        return
    mid=(start+end)//2
    lazy_update(2*node+1,start,mid,us,ue,val)
    lazy_update(2*node+2,mid+1,end,us,ue,val)
    tree[node]=tree[2*node+1]+tree[2*node+2]

n=6
arr=[1,3,5,7,9,11]
tl=2*(2**ceil(log2(n)))-1
tree=[0]*tl
build(0,0,n-1)
lazy=[0]*tl
print(lazy_query(0,0,5,1,3))
lazy_update(0,0,5,1,4,2)
print(lazy_query(0,0,5,1,3))


