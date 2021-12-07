import random,time,math

def partition(arr,p,r):
    x = arr[r]
    i = p
    for j in range(p,r,1):
        if arr[j] < x:
            c = arr[i]
            arr[i] = arr[j]
            arr[j] = c
            i = i + 1
    c = arr[i]
    arr[i] = arr[r] 
    arr[r] = c
    return i

def quick_sort(arr,p,r):
    if p < r:
        q = partition(arr,p,r)
        quick_sort(arr,p,q-1)
        quick_sort(arr,q+1,r)

def quick(n):
    start_time = time.time()
    arr = []
    iterations = n
    for i in range(0,iterations):
        ran = random.randint(0,iterations*iterations)
        arr.append(ran)
    #arr = [6,3,1,8,2,7,9,1,2]  #[1,2,3,6,7,8]
    #print(arr)
    quick_sort(arr,0,len(arr)-1)
    #print(arr)
    end_time = time.time()
    return end_time - start_time
    

average_times = 20
total = 0
n = 50000
for i in range(0,20):
    total = total + quick(n)

complexity = n*(math.log(n,2))
accurate = total/average_times
print(f"average time taken: {accurate}s")
print(f"n*logn : {complexity}")
print(f"time/(n*logn) : {accurate/complexity}")
