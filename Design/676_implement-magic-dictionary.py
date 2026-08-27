"""
LeetCode 676: Implement Magic Dictionary
URL: https://leetcode.com/problems/implement-magic-dictionary/
Difficulty: Medium
Category: Hash Table, String, Depth-First Search, Design, Trie

Approach:
The implementation uses a brute-force approach, storing all dictionary words directly and performing a linear scan for each search query.

Key Observation:
The core design decision is to store the entire dictionary as a list and then iterate through each word to check for a single character difference with the search word.

Complexity:
- Time Complexity: O(N * L_max) (The `search` method iterates through N dictionary words, and for each word, it performs a character-by-character comparison up to L_max characters (where L_max is the maximum word length). The `buildDict` method is O(1) as it just assigns a reference to the input list.)
- Space Complexity: O(S_total) (The `MagicDictionary` stores all input dictionary words in a list, requiring space proportional to the total number of characters (S_total) across all words.)
"""

# --- LEETVAULT CODE START ---
class MagicDictionary:

    def __init__(self):
        self.d=[]
    def buildDict(self, dictionary: List[str]) -> None:
        self.d=dictionary
        return 
    def search(self, searchWord: str) -> bool:
        for i in self.d:
            if len(i)==len(searchWord):
                c=0
                for i,j in zip(i,searchWord):
                    if i!=j:
                        c+=1
                if c==1:
                    return True
        return False                    


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)