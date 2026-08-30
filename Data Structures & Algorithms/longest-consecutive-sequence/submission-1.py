class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums1 = set(nums)
        maxi = 0
        for num in nums1:
            if num-1 not in nums1:
                c = 1
                while num+c in nums1:
                    c += 1
                maxi = max(maxi, c)
        return maxi
            


