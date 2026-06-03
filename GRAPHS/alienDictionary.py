from collections import defaultdict, deque
# code here
words = ["baa", "abcd", "abca", "cab", "cad"]
graph=defaultdict(list)
chars=set()
for i in words:
    for ch in i:
        chars.add(ch)
for i in range(len(words)-1):
    w1=words[i]
    w2=words[i+1]
    if len(w1) > len(w2) and w1.startswith(w2):
        print("")
        break
    for j in range(min(len(w1),len(w2))):
        if w1[j]!=w2[j]:
            graph[w1[j]].append(w2[j])
            break
indeg={ch:0 for ch in chars}
q=deque([])
for i in graph:
    for j in graph[i]:
        indeg[j]+=1
for i in indeg:
    if indeg[i]==0:
        q.append(i)
order=""
while q:
    cur=q.popleft()
    order+=cur
    for nei in graph[cur]:
        indeg[nei]-=1
        if indeg[nei]==0:
            q.append(nei)
if len(order) != len(chars):
    print("")
else:
    print(order)            
