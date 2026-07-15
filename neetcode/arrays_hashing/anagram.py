from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = Counter(s)
        countT = Counter(t)
        print(countS)
        return countS == countT
sol = Solution()
out = sol.isAnagram("jam","jam")
print(out)