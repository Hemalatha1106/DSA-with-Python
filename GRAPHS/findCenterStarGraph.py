#followed classic step but inefficient,refer leetcode discussion tab.
#leetcode 1791
from collections import defaultdict
edges = [[1,2],[2,3],[4,2]]
d = defaultdict(set)
for i,j in edges:
    d[i].add(j)
    d[j].add(i)
for i in d:
    if len(d[i]) == len(d)-1:
        print(i, end = " ")
        exit()