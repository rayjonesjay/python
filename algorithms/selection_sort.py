# selection sort algorithm

def selection(arr):
    n = len(arr)
    for i in range(n-1):
        mini = i 
        for j in range(n):
            if (arr[j] < arr[mini]):
                mini = j
        if not mini ==  i:
            arr[i] , arr[mini] = arr[mini], arr[i]
    return arr 

arr = [3,5,1,7,2]
print(selection(arr))
