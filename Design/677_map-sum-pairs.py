"""
LeetCode 677: Map Sum Pairs
URL: https://leetcode.com/problems/map-sum-pairs/
Difficulty: Medium
Category: Hash Table, String, Design, Trie

Approach:
This implementation uses a hash map (Python dictionary) to store all key-value pairs directly. The `insert` operation stores or updates a key-value entry, while the `sum` operation iterates through every stored key to find those that begin with the given prefix.

Key Observation:
The primary design decision is the use of a simple hash map, which offers average O(L) time complexity for `insert` operations (where L is the key length). However, this choice results in an inefficient `sum` operation, as it requires a linear scan through all stored keys to check for prefix matches.

Complexity:
- Time Complexity: O(L_key) for insert; O(N * P) for sum (`insert` takes time proportional to the key length `L_key` for hashing. `sum` iterates through `N` stored keys, performing a string slice and comparison of length `P` for each, resulting in O(N * P).)
- Space Complexity: O(N * L_avg) (The dictionary `self.d` stores `N` distinct keys, where each key has an average length of `L_avg`, consuming O(N * L_avg) space along with the integer values.)
"""

# --- LEETVAULT CODE START ---
class MapSum:

    def __init__(self):
        self.d={}

    def insert(self, key: str, val: int) -> None:
        self.d[key]=val
        return
    def sum(self, prefix: str) -> int:
        l=len(prefix)
        s=0
        for i in self.d:
            if i[:l]==prefix:
                s+=self.d[i]
        return s             


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)