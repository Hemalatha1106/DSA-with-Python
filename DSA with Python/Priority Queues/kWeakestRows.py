mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k = 3
# this is hashmap based solution
# a = dict()
# for i in range(len(mat)):
#     a[i] = mat[i].count(1)
# a = dict(sorted(a.items(),key= lambda x: x[1]))
# res = list(a.keys())
# print(res[:k]) 
    
import heapq
heap = []  # max-heap using negatives

for i, row in enumerate(mat):
    strength = row.count(1)

    # push negative strength so heap behaves like max-heap
    heapq.heappush(heap, (-strength, -i))

    # keep only k weakest
    if len(heap) > k:
        heapq.heappop(heap)

# extract rows (reverse order because max-heap)
res = []
while heap:
    strength, idx = heapq.heappop(heap)
    res.append(-idx)

res.reverse()  # weakest first
print(res)

