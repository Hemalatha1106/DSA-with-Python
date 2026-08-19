"""
LeetCode 752: Open the Lock
URL: https://leetcode.com/problems/open-the-lock/
Difficulty: Medium
Category: Array, Hash Table, String, Breadth-First Search, Bidirectional Search

Approach:
This implementation uses Breadth-First Search (BFS) to find the shortest path from the starting lock combination "0000" to the target combination. It treats each 4-digit combination as a node in an unweighted graph, exploring one layer at a time to determine the minimum number of turns.

Key Observation:
Converting the `deadends` list to a `set` allows for O(1) average-time lookups, significantly optimizing checks against invalid combinations. A `visited` set prevents revisiting states, ensuring the shortest path is found and avoiding redundant computations.

Complexity:
- Time Complexity: O(N * D) (The BFS algorithm visits each of the N=10^4 possible lock combinations at most once. For each visited combination, it generates 8 neighbors, each involving string manipulations of length D=4, and performs constant-time set lookups and queue operations.)
- Space Complexity: O(N * D + M * D) (The `q` (queue) and `visited` set can store up to N=10^4 lock combinations (each a string of length D=4). The `deadends` set stores up to M deadend combinations (M <= N), also strings of length D=4.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def tr(s):
            if s=="9":
                return "0"
            return str(int(s)+1)        
        def tl(s):
            if s=="0":
                return "9"
            return str(int(s)-1)    
        def build(s):
            s=list(s)
            ans=[]
            for n in range(4):
                temp=s[n]
                s[n]=tr(temp)
                ans.append("".join(s))
                s[n]=tl(temp)
                ans.append("".join(s))
                s[n]=temp
            return ans    
        strt="0000"
        q=deque([strt])
        visited={strt}
        deadends=set(deadends)
        d=0
        while q:
            l=len(q)                            
            for i in range(l):
                cur=q.popleft()
                if cur in deadends:
                    continue
                if cur==target:
                    return d
                t=build(cur)
                for e in t:
                    if e not in visited and e not in deadends:
                        q.append(e)
                        visited.add(e)
            d+=1        
        return -1            