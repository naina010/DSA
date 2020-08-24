from bisect import bisect_right

def job_schedule(t,p):
    dp=p[:]
    finish=[]
    for e in t: finish.append(e[1])

    jobs=[list(t[i])+[p[i]] for i in range(len(t))]
    jobs.sort(key = lambda j:j[1])           # jobs sorted according to end times
    for i in range(1,len(t)):
        x = bisect_right(finish, jobs[i][0])
        if x>0:
            dp[i]=max(dp[i]+dp[x-1], dp[i-1])
        else:
            dp[i]=max(dp[i], dp[i-1])

    print('Maximum profit',dp[-1])


time=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
profit=[5,6,5,4,11,2]
job_schedule(time,profit)
