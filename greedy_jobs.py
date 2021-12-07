#the below function makes sure that the user gets the max
#profit from completing the jobs and the profit of the
#unfinished jobs will be neglected
def greedy_max_profit(jobs,slots): #jobs = job-deadline-profit
    jobs_sorted = sorted(jobs,key=lambda x: -x[2])
    slot = []
    profit = 0
    for i in range(0,slots):
        slot.append(0)
    for job in jobs_sorted:
        deadline = job[1]
        for i in range(deadline-1,-1,-1):
            if slot[i] == 0:
                slot[i] = job[0]
                profit = profit + job[2]
                break
    return slot,profit

#for below function it makes sure that the penalty of
#the unfinished jobs will be minimum and the penalty 
#finished tasks will be negelected
def greedy_min_penalty(jobs,slots): #jobs = job-deadline-loss
    jobs_sorted = sorted(jobs,key=lambda x: -x[2])
    slot = []
    penalty = 0
    loss = 0
    for job in jobs_sorted:
        penalty = penalty + job[2]
    for i in range(0,slots):
        slot.append(0)
    for job in jobs_sorted:
        deadline = job[1]
        for i in range(deadline-1,-1,-1):
            if slot[i] == 0:
                slot[i] = job[0]
                loss = loss + job[2]
                break
    penalty = penalty - loss
    return slot,penalty

#the below function returns the deadline of the job which
#has longest deadline i.e longest deadline in the list
def max_deadline(jobs):
    return max(jobs,key = lambda x:x[1])[1]

#     job-deadline-profit
jobs = [["a",2,100],
        ["b",1,19],
        ["c",2,27],
        ["d",1,25],
        ["e",3,15]]
#             job-deadline-penalty
jobs_penalty = [["job-1",2,10],
                ["job-2",3,19],
                ["job-3",2,27],
                ["job-4",1,25],
                ["job-5",3,15]]

slots,profit = greedy_max_profit(jobs,max_deadline(jobs))
print("Maximum Profit:",slots,profit)
slot,loss = greedy_min_penalty(jobs_penalty,max_deadline(jobs_penalty))
print("Minimum Loss:",slot,loss)

        
