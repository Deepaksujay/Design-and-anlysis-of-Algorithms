#solved using greedy method

def sort(values,weights):
    leng = len(values)
    if len(weights) == leng:
        all = []
        for i in range(0,leng):
            den = values[i]//weights[i]
            all.append([values[i],weights[i],den])
        return sorted(all, key=lambda x: -x[2])

def greedy(main,max,n):
    if n < len(main):
        weight = main[n][1]
        if weight > max:
            return max*main[n][2]
        else:
            total = main[n][0] + greedy(main,max-weight,n+1)
            return total




weights = [20 , 10 , 30]
values = [100 , 60 , 120]
CAPACITY = 50
main_array = sort(values,weights)
print(main_array)
print(greedy(main_array,CAPACITY,0))