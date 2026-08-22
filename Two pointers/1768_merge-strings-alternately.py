"""
LeetCode 1768: Merge Strings Alternately
URL: https://leetcode.com/problems/merge-strings-alternately/
Difficulty: Easy
Category: Two Pointers, String

Approach:
The algorithm uses two pointers to iterate through both input strings, `word1` and `word2`, and builds the result string by alternately appending characters.

Key Observation:
The key design is using independent `if` conditions within the loop to alternately append characters, allowing it to continue processing the longer string's remaining characters after the shorter one is exhausted.

Complexity:
- Time Complexity: O(N + M) (The loop iterates a total of `N + M` times (where N and M are the lengths of word1 and word2), processing each character exactly once, leading to linear time complexity for string construction.)
- Space Complexity: O(N + M) (A new string `res` is created to store the merged output, which has a length equal to the sum of the lengths of the input strings.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=r=0
        res=""
        while l<len(word1) or r<len(word2):
            if l<len(word1):
                res+=word1[l]
                l+=1
            if r<len(word2):
                res+=word2[r]
                r+=1
        return res            