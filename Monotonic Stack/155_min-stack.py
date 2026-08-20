"""
LeetCode 155: Min Stack
URL: https://leetcode.com/problems/min-stack/
Difficulty: Medium
Category: Stack, Design

Approach:
This implementation uses two internal lists, simulating two stacks: one (`st`) for standard stack operations and another (`mnst`) specifically designed to track the minimum element.

Key Observation:
The auxiliary minimum stack (`mnst`) maintains its invariant such that its top element is always the current minimum of the main stack, achieved by pushing a value only if it's less than or equal to the current minimum and popping it only when the corresponding value is removed from the main stack.

Complexity:
- Time Complexity: O(1) (All operations (push, pop, top, getMin) involve constant-time list appends, pops, and direct index lookups, leading to amortized O(1) time complexity.)
- Space Complexity: O(N) (In the worst-case scenario, both the main stack and the auxiliary minimum stack will store up to N elements, where N is the total number of elements pushed onto the stack.)
"""

# --- LEETVAULT CODE START ---
class MinStack:

    def __init__(self):
        self.st=[]
        self.mnst=[]

    def push(self, value: int) -> None:
        self.st.append(value)
        if not self.mnst or self.mnst[-1]>=value:
            self.mnst.append(value)
        return    

    def pop(self) -> None:
        if self.mnst and self.mnst[-1]==self.st[-1]:
            self.mnst.pop()
        return self.st.pop()    

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mnst[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()