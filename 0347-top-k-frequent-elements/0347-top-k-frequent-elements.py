class Solution(object):
    def topKFrequent(self, nums, k):
        itog = []
        chisla = {}
        dildo = []
        if len(nums) == 1:
            itog.append(nums[0])
            return itog

        for num in nums:
            if num in chisla:
                chisla[num] += 1
            else:
                chisla[num] = 1
        
        for chlen, kolvo in chisla.items():
            dildo.append([kolvo, chlen])

        dildo.sort(reverse = True)

        for i in range(k):
            itog.append(dildo[i][1])
        
        return itog      