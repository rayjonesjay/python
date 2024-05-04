"""
leetcode 2956
"""

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = 0
        y = 0
        nums1set=set(nums1)
        nums2set=set(nums2)
        for n1 in nums1:
            if n1 in nums2set:
                x+=1
        for n2 in nums2:
            if n2 in nums1set:
                y+=1
        return x,y
