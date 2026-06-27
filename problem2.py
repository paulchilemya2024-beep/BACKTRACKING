# Given two integers n and k, return all possible combinations of k numbers
# chosen from the range [1, n].
# You may return the answer in any order.

# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
from typing import List
class Solution(object):
    def combine(self, n:int, k:int)->List[List[int]]:
       

        result = []
        path = []

        def backtracking(start):
            if len(path)==k:
                result.append(path[:])
                return 
            for num in range(start, n+1):
                path.append(num)
                backtracking(num+1)
                path.pop()
        backtracking(1)
        return result

test1 = Solution().combine(6,3)
print(test1)

        