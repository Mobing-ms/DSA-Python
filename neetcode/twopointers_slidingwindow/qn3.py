class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l,r = 0,1
        maxlen = 0
        if n == 1:
            return 1
        if n == 2:
            if s.count(s[0]) >= 2:
                return 1
            return 2
            
        while r < n:
            if s[l:r+1].count(s[r]) >= 2:
                maxlen = max(maxlen,r-l)
                l+=1
                continue
            else:
                r+=1
                maxlen = max(maxlen,r-l)
                    
        return maxlen
#memory usage is quiet ok
#time complexity could be improved using the set 
            
                
                