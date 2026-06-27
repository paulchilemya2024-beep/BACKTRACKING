# LEETCODE 78
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

from typing import List
class Solution:
    def subsets(self, nums:List[int])-> List[List[int]]:
        result = [] #where all subsets will be stored
        path = [] #the current subset you are building

        def backtrack(start):
            result.append(path[:]) #creates shallow copy of path

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1)
                path.pop()
        backtrack(0)
        return result

x= [1,2,3,4]
test = Solution().subsets(x)
print(test)