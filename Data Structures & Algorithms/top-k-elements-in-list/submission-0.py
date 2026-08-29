class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = {}
        for i in range(len(nums)):
            if nums[i] not in c:
                c[nums[i]] = 1
            else:
                c[nums[i]]= c.get(nums[i], 0) + 1
        c_f = dict(sorted(c.items(), key=lambda x: x[1], reverse=True)[:k])
        return [j for j, v in c_f.items()]