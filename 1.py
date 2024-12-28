# https://leetcode.com/problems/two-sum/description/

"""
- We're going to rely on the relationship between addition and subtraction
- Suppose we have two numbers a + b = target
    - This means that a = target - b
    - And b = target - a

- For any given number, 
    the number to be added to it to get a target is the target - that number
    let's refer to this as the compliment.

- For this question, we'll go through the nums array and keep track of each number and idx
- because each number could be a possible compliment to a later number

- for each number we'll check if we've seen its compliment before, if yes, then we've the soln
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in mapp:
                return [mapp[difference], i]

            mapp[nums[i]] = i

        # Time: O(n)
        # Space: O(n)
