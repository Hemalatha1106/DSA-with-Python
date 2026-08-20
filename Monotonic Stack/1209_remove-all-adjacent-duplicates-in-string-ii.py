"""
LeetCode 1209: Remove All Adjacent Duplicates in String II
URL: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
Difficulty: Medium
Category: String, Stack

Approach:
This implementation uses a stack to store characters along with their consecutive counts. It iterates through the input string, updating counts or adding new characters to the stack, and automatically removes characters from the stack once their count reaches 'k'.

Key Observation:
The key design is the use of a stack where each element is a pair `[character, count]`, allowing efficient O(1) updates and removals of adjacent duplicates as they are encountered in a single pass.

Complexity:
- Time Complexity: O(N) (The code iterates through the input string once, performing amortized O(1) stack operations per character, and then iterates through the stack to build the result string, where total characters are at most N.)
- Space Complexity: O(N) (The stack stores at most N `[character, count]` pairs in the worst case, and the resulting string can also contain up to N characters.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st=[]
        for i in s:
            if not st or st[-1][0]!=i:
                st.append([i,1])
            elif st and st[-1][0]==i:
                st[-1][1]+=1
            if st[-1][1]==k:
                st.pop()
        res=""
        for i,j in st:
            res+=i*j
        return res                    