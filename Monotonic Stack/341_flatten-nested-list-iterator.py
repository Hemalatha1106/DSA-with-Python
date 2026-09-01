"""
LeetCode 341: Flatten Nested List Iterator
URL: https://leetcode.com/problems/flatten-nested-list-iterator/
Difficulty: Medium
Category: Stack, Tree, Depth-First Search, Design, Queue, Iterator

Approach:
The implementation uses an iterative depth-first search (DFS) approach, simulated with a stack, to flatten the nested list structure. It pre-populates the stack with the initial list elements in reverse order and maintains the processing order through strategic pushing and popping.

Key Observation:
The `hasNext()` method is crucial; it eagerly processes nested lists by popping them from the stack and pushing their elements back onto the stack in reverse order until the top of the stack is guaranteed to be a single integer. This ensures `next()` always retrieves an integer efficiently.

Complexity:
- Time Complexity: O(N) (Each `NestedInteger` object (whether an integer or a list) is pushed onto the stack and popped from it at most once across all calls to `__init__`, `hasNext`, and `next`. Operations on these objects are constant time in terms of structure traversal.)
- Space Complexity: O(N) (In the worst case, the stack `self.st` may need to store references to all `NestedInteger` objects (both integers and nested lists) that are currently awaiting processing, proportional to the total number of elements in the entire flattened structure.)
"""

# --- LEETVAULT CODE START ---
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.st=[]
        for i in nestedList[::-1]:
            self.st.append(i)
    
    def next(self) -> int:
        self.hasNext()
        return self.st.pop()
    
    def hasNext(self) -> bool:
        while self.st and not self.st[-1].isInteger():
            cur=self.st.pop()
            for i in cur.getList()[::-1]:
                self.st.append(i)
        return len(self.st)>0


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())