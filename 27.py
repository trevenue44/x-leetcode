# https://leetcode.com/problems/remove-element/description/

"""
Even though the question talks about removing elements, it doesn't mean we should actually remove the elements. 

nums = [0,1,2,2,3,0,4,2], val = 2

The goal is to make sure that we modify the `nums` list in-place such that the first `k` elements are not equal to the `val` to remove. 
This means that we can move all elements that are equal to `val` to the end of the list, 
and then return the count of the other elements from the start to the point where the `val` elements start to repeat at the end.

For the example above, 
we can move all 2s to the end of the list by swapping them with another element at the end that is not equal to `val`.
(yes, we need to ensure that the element we're swapping with at the end, is not equal to `val` else we'd just waste our time)

So we can:
1. swap the first 2 with the 4 at the end: [0,1,4,2,3,0,2,2]
2. then swap the next 2 with the 0 at the end: [0,1,4,0,3,2,2,2]

Once this is done, the `nums` list would have all elements that are NOT equal to `val` coming first; 
before the rest that ARE equal to `val` would all be repeating at the end.

The next thing we need to do now is to just count the number of non- `val` elements and return that as k. 
So we count from the beginning to the point we encounter the first `val` element.
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        j = n - 1

        # swapping elements to move all `val` elements to the end of the list
        while i < n and i < j:
            if nums[i] == val:
                if nums[j] != val:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                j -= 1
            else:
                i += 1

        # counting the number of non-`val` elements that come first in nums as k
        k = 0
        for num in nums:
            if num != val:
                k += 1
            else:
                break

        return k

        # Time: O(n)
        # Space: O(1)
