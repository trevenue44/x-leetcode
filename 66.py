# https://leetcode.com/problems/plus-one/description/

"""
Here, we're going to adopt the concept of addition in math.

 459
+  1
-----
 460
-----

We add from right to left. 
For each sum, there's a place value which is the actual value for that place and then there's a carry-on which is moved on and added to the next place.

In the example above, when we add the units place 9 + 1, we get 1 0. 
The 0 is the resulting units place value.
The 1 is then carried on to be added to the 5 at the tens place, resulting in the 6. 
    - Note: same carry-on and place value concept is applied to the resulting 6 at the tens position

We're going to write a loop to go over the array of digits from right to left.
For each place, we'll update the value with the place value and keep track of the carry-on value to be used for the next place.
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry_on = 1
        for i in range(-1, -len(digits) - 1, -1):
            summ = digits[i] + carry_on
            carry_on = summ // 10
            digits[i] = summ % 10

        if carry_on:
            digits.insert(0, carry_on)

        return digits

        # Time: O(n)
        # Space: O(1)
