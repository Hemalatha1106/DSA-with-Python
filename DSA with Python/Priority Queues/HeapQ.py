import heapq
arr = [10, 20, 5, 6, 1, 8]
arr2 = arr.copy()
max_heap = [-x for x in arr]
heapq.heapify(max_heap)

print("Max heap:", max_heap)
heapq.heappush(max_heap,-40)
max_val = -heapq.heappop(max_heap)
print(max_val)

heapq.heapify(arr2)
print(arr2)
heapq.heappush(arr2,0)
print(arr2)
m = heapq.heappop(arr2)
print(m)
