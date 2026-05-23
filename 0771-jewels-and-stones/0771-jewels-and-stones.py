class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        kolvo = 0
        
        for stone in stones:
            for jew in jewels:
                if stone == jew:
                    kolvo += 1
        return kolvo