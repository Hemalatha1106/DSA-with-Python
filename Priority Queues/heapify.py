def max_heap(arr,n,i):
    left_child = 2*i+1
    right_child = 2*i+2
    largest = i
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heap(arr,n,largest) 
def min_heap(arr,n,i):
    smallest = i
    left_child = 2*i+1
    right_child = 2*i+2
    if left_child < n and arr[left_child] < arr[smallest]:
        smallest = left_child
    if right_child < n and arr[right_child] < arr[smallest]:
        smallest = right_child
    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        min_heap(arr,n,smallest)
arr = [10,20,5,6,1,8]
arr1 = arr.copy()
n = len(arr)
for i in range(n//2-1,-1,-1):
    max_heap(arr,n,i)
print(arr)    
for i in range(n//2-1,-1,-1):
    min_heap(arr1,n,i)   
print(arr1)                                     