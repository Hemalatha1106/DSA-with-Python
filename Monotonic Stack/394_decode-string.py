"""
LeetCode 394: Decode String
URL: https://leetcode.com/problems/decode-string/
Difficulty: Medium
Category: String, Stack, Recursion

Approach:
This implementation uses an iterative approach with a stack to process the input string.

Key Observation:
The stack stores both numeric multipliers and partially decoded string segments, allowing the algorithm to manage and reconstruct nested encoded strings by pushing context upon '[' and unwinding upon ']'.

Complexity:
- Time Complexity: O(L_output) (Each character of the final decoded string (L_output) is effectively constructed and appended to an intermediate string exactly once throughout the entire process.)
- Space Complexity: O(L_output) (In the worst-case, the stack may store partial decoded strings whose combined length is proportional to the length of the final decoded string.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        n=0
        for i in s:
            if i.isdigit():
                n=n*10+int(i)
            elif i=="[":
                st.append(n) 
                st.append("")
                n=0
            elif i=="]":
                ch=st.pop()
                m=st.pop()
                d=ch*m
                if st:
                    st[-1]+=d
                else:
                    st.append(d)
            else:
                if st:
                    st[-1]+=i
                else:
                    st.append(i)
        return st[0]                                   