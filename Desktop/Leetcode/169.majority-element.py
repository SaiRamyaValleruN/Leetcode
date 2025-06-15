#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count =0
        for x in nums:
            if count == 0 :
                candidate = x
                count =1
            elif x== candidate :
                count +=1
            else:
                count -=1
        return candidate
# @lc code=end

