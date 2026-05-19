class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        chisla = {}
        itog = []

        if len(nums) == 1:
            itog.append(nums[0])
            return itog

        else:

            for num in nums:
                if num in chisla:
                    chisla[num] += 1
                else:
                    chisla[num] = 1
        
            for i in chisla:
                if chisla[i] > len(nums) // 3:
                    itog.append(i)
        return itog
        