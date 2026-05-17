class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        kolvo = {}

        if len(nums) == 1:
            return nums[0]

        for num in nums:
            if num in kolvo:
                kolvo[num] += 1
            else:
                kolvo[num] = 1

            if kolvo[num] > len(nums) // 2:
                return num