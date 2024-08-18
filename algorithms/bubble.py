# bubble sort algorithm

def bubble(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n):
            if arr[i] < arr[j]:
                arr[i] , arr[j] = arr[j] , arr[i]
    return arr

arr = [3,2,5,6,4]
print(bubble(arr))