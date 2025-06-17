#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        hashset = set(nums1)

        result = []
        for i in nums2:
            if i in hashset :
                result.append(i)
                hashset.remove(i)
        return result
# @lc code=end

