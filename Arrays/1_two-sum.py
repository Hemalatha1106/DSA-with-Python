"""
LeetCode 1: Two Sum
URL: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Category: Array, Hash Table

Approach:
The algorithm iterates through the input array, calculating the required complement for each number and checking if it has been encountered previously.

Key Observation:
Utilizing a hash map (dictionary) allows for efficient O(1) average-time lookups to determine if a complement exists among the already processed numbers.

Complexity:
- Time Complexity: O(N) (The solution involves a single pass through the `nums` array, with hash map operations taking O(1) average time per element.)
- Space Complexity: O(N) (A hash map is used to store up to N numbers and their indices, consuming space proportional to the input array size in the worst case.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=defaultdict(int)
        for i in range(len(nums)):
            s=target-nums[i]
            if s in d:
                return [d[s],i]
            d[nums[i]]=i    