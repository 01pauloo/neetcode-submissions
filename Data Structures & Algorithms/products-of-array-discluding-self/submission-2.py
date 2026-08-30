class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        pref = [1] * len(nums)
        for i in range(len(nums)): # tableau des produits avant i
            if i == 0:
                pref[i] = 1
            else:
                pref[i] = pref[i-1] * nums[i-1]

        suff = [ 1 for k in range(len(nums))]
        for i in range(len(nums)-1, -1, -1): # tableau des produits après i 
            if i == len(nums)-1 :
                suff[i] = 1
            else:
                suff[i] = suff[i+1] * nums[i+1]
        for i in range(len(nums)):
            output.append(pref[i]*suff[i])
        return output
