"""
LeetCode 146: LRU Cache
URL: https://leetcode.com/problems/lru-cache/
Difficulty: Medium
Category: Hash Table, Linked List, Design, Doubly-Linked List

Approach:
The implementation combines a hash map to store key-to-node mappings with a doubly-linked list to maintain the order of usage, allowing for efficient access and removal of least recently used items.

Key Observation:
Using a hash map for O(1) average-time lookups to retrieve nodes and a doubly-linked list for O(1) removal and insertion operations enables constant-time average performance for cache operations.

Complexity:
- Time Complexity: O(1) (All operations like `get` and `put` involve constant-time hash map lookups/updates and constant-time doubly-linked list manipulations (inserting, removing, or moving nodes).)
- Space Complexity: O(capacity) (The `cache` dictionary stores up to `capacity` key-value pairs, and the doubly-linked list holds `capacity` `DLL` nodes, each consuming constant space.)
"""

# --- LEETVAULT CODE START ---
class DLL:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.left=DLL(0,0)
        self.right=DLL(0,0)
        self.left.next=self.right
        self.right.prev=self.left

    def insert(self,node):
        nxt=self.left.next
        self.left.next=node
        node.next=nxt
        node.prev=self.left
        nxt.prev=node

    def remove(self,node):
        nxt=node.next
        prv=node.prev
        prv.next=nxt
        nxt.prev=prv    

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val   

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node=DLL(key,value) 
        self.cache[key]=node
        self.insert(node)
        if len(self.cache)>self.capacity:
            last=self.right.prev
            self.remove(last)
            del self.cache[last.key]


           



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)