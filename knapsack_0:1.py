#Dynamic programming approach

def sort(values,weights):
    leng = len(values)
    if len(weights) == leng:
        all = []
        for i in range(0,leng):
            all.append([values[i],weights[i]])
        return sorted(all, key=lambda x: -x[0])


def knapsack(max_,main,n):
    if n >= len(main) or max_ == 0:
        return 0
    if (main[n][1] > max_):
        return knapsack(max_,main,n+1)
    else:
        return max(
            main[n][0] + 
            knapsack(max_-main[n][1],main,n+1),
            knapsack(max_,main,n+1))


weights = [20 , 10 , 30]
values = [100 , 60 , 120]
CAPACITY = 50
main_array = sort(values,weights)
print(main_array)
print(knapsack(CAPACITY,main_array,0))
