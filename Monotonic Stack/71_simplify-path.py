"""
LeetCode 71: Simplify Path
URL: https://leetcode.com/problems/simplify-path/
Difficulty: Medium
Category: String, Stack

Approach:
This implementation uses a stack to process each component of the path, pushing valid directory names, popping for parent directories ('..'), and ignoring current directory ('.') or empty components.

Key Observation:
The stack data structure is effectively used to maintain the canonical path by simulating directory traversals: pushing new directories and popping when navigating up using '..'.

Complexity:
- Time Complexity: O(L) (Splitting the path takes O(L) time, where L is the path string length. The loop iterates through path components, performing O(1) stack operations. Finally, joining the components takes O(L) time.)
- Space Complexity: O(L) (The `split()` operation creates a list of path components taking O(L) space, and the stack can store up to O(L) characters in the worst-case scenario.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def simplifyPath(self, path: str) -> str:
        st=[]
        path=path.split("/")
        for i in path:
            if i=="" or i==".":
                continue
            elif i=="..":
                if st:
                    st.pop()
            else:
                st.append(i)
        res="/"
        return res+"/".join(st)

