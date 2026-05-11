class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist,tlist=list(s),list(t)
        if sorted(slist) == sorted(tlist):
            return True
        return False    