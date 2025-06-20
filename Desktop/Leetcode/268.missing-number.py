#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len (nums)
        expected = n * (n+1)//2
        actual = sum(nums)
        return expected - actual
        
# @lc code=end

