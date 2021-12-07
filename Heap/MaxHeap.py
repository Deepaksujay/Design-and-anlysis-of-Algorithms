def Max_Heapify(arr,i):
    l = 2*i + 1
    r = l + 1
    if (l < len(arr)) and (arr[l]>arr[i]):
        largest = l
    else:
        largest = i
    if (r < len(arr)) and (arr[r]>arr[largest]):
        largest = r
    if (largest != i):
        arr[i] = arr[i] + arr[largest]
        arr[largest] = arr[i] - arr[largest]
        arr[i] = arr[i] - arr[largest]
        Max_Heapify(arr,largest)

def Heap_Sort(arr):
    for i in range(int((len(arr)/2)-1),-1,-1):
        Max_Heapify(arr,i)

arr = [1,8,2,6,5,3,4,11,9]
Heap_Sort(arr)
print(arr)

#print(Not_Heapified(arr,0))