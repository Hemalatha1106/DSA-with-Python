"""
LeetCode 735: Asteroid Collision
URL: https://leetcode.com/problems/asteroid-collision/
Difficulty: Medium
Category: Array, Stack, Simulation

Approach:
This implementation uses a stack to simulate asteroid collisions. It iterates through each asteroid, resolving potential collisions with asteroids already on the stack before appending the current asteroid if it survives.

Key Observation:
The stack data structure is crucial as it maintains the order of surviving asteroids, allowing efficient comparison between an incoming left-moving asteroid and previously encountered right-moving asteroids at the top of the stack.

Complexity:
- Time Complexity: O(N) (Each asteroid is pushed onto the stack at most once and popped from the stack at most once, leading to an overall linear time complexity.)
- Space Complexity: O(N) (In the worst case, the stack may store all asteroids if no collisions occur (e.g., all asteroids move in the same direction), requiring space proportional to the input size N.)
"""

# --- LEETVAULT CODE START ---
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for i in asteroids:
            a=True
            while st and st[-1]>0 and i<0:
                if abs(i)>st[-1]:
                    st.pop()
                elif abs(i)==st[-1]:
                    st.pop()
                    a=False
                    break
                else:
                    a=False
                    break
            if a:
                st.append(i)
        return st        