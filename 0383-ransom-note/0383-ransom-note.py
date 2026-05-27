class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ls1 = {}
        ls2 = {}
        for l in ransomNote:
            if l in ls1:
                ls1[l] += 1
            else:
                ls1[l] = 1
        for l in magazine:
            if l in ls2:
                ls2[l] += 1
            else:
                ls2[l] = 1
        for le in ls1:
            if le not in ls2:
                return False
            if ls1[le] > ls2[le]:
                return False
        return True 
        