class Solution(object):
    def singleNumber(self, nums):

        chisla = {}

        if len(nums) == 1:
            return nums[0]
        
        for num in nums:
            if num in chisla:
                chisla[num] += 1
            else:
                chisla[num] = 1
        
        for ch in chisla:
            if chisla[ch] == 1:
                return ch
