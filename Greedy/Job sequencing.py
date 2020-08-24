
def job_sequence(jobs, n):
    slot = [0]*(n+1)
    jobs.sort(key=lambda x: x[2], reverse=True)  # jobs => [job_name, deadline, profit]
    seq = []
    for i in range(n):
        for j in range(min(n, jobs[i][1]), 0, -1):
            if slot[j] == 0:
                slot[j] = 1
                seq.append([j, jobs[i][0]])
                break
    seq.sort()
    return seq

