"""
LeetCode 210: Course Schedule II
URL: https://leetcode.com/problems/course-schedule-ii/
Difficulty: Medium
Category: Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort

Approach:
The algorithm implements Kahn's algorithm for topological sorting, which uses a Breadth-First Search (BFS) approach to determine a valid order of courses based on their prerequisites.

Key Observation:
It efficiently manages course dependencies by tracking in-degrees for all courses and using a queue to process courses that have no pending prerequisites, ensuring that a course is only processed once all its prerequisites are met.

Complexity:
- Time Complexity: O(V + E) (Building the adjacency list and in-degree array takes O(V + E) time, and each course and prerequisite is processed exactly once during the BFS traversal.)
- Space Complexity: O(V + E) (The adjacency list, in-degree array, queue, and result list all require space proportional to the number of courses (V) and prerequisites (E).)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d=defaultdict(list)
        indeg=[0]*numCourses
        for i,j in prerequisites:
            d[j].append(i)
            indeg[i]+=1
        q=deque([])
        for i in range(numCourses):
            if indeg[i]==0:
                q.append(i)
        res=[]
        while q:
            cur=q.popleft()
            res.append(cur)
            for nei in d[cur]:
                indeg[nei]-=1
                if indeg[nei]==0:
                    q.append(nei)
        return res if len(res)==numCourses else []           
