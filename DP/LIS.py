# 1nov19
# Longest Increasing Subsequence length DP
# O(n^2)

def lis(a):
    n=len(a)
    dp=[1 for e in a]
    for i in range(1,n):
        for j in range(i):
            if a[j]<a[i]:
                dp[i]=max(dp[i],dp[j]+1)
    print('length of LIS:',dp[-1])
    # print('LIS:',)

a=[3,4,-1,0,6,2,3]
lis(a)
