class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        kolvo = 0
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] == nums[j]:
                    if i < j:
                        kolvo += 1
        return kolvo