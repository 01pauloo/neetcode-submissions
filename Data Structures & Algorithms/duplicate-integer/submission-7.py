class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        valeurs = dict()
        for i in range(len(nums)):
            if nums[i] in valeurs:
                return True
            else:
                valeurs[nums[i]] = True
        return False

            

                
            