"""
LeetCode 901: Online Stock Span
URL: https://leetcode.com/problems/online-stock-span/
Difficulty: Medium
Category: Stack, Design, Monotonic Stack, Data Stream

Approach:
This implementation uses a monotonic stack to calculate the span for each new stock price.

Key Observation:
The stack stores pairs of `[price, span]`, where `span` represents the number of consecutive previous days (including itself) for which the price was less than or equal to the current day. When processing a new price, it efficiently sums the pre-calculated spans of all smaller or equal preceding prices by popping them from the stack.

Complexity:
- Time Complexity: O(1) amortized (Each stock price is pushed onto the stack exactly once and popped from the stack at most once across all calls to `next()`, resulting in an amortized constant time complexity per call.)
- Space Complexity: O(N) (In the worst case, such as a strictly decreasing sequence of prices, the stack may store all N historical prices and their associated spans.)
"""

# --- LEETVAULT CODE START ---
class StockSpanner:

    def __init__(self):
        self.st=[]

    def next(self, price: int) -> int:
        res=0
        self.st.append([price,1])
        c=0
        while self.st and self.st[-1][0]<=price:
            p,s=self.st.pop()
            c+=s
        res+=c
        self.st.append([price,c])    
        return res    


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)