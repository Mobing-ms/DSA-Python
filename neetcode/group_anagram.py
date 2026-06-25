from collections import Counter

class Solution:
    def groupAnagrams(self, strs):
        count = []
        new_list = []
        for i,word in enumerate(strs):
            count[i] = Counter(word)
        
        return count

sol = Solution()
out_list = sol.groupAnagrams(['eat' ,'ate' ,'akshay' ,'sachu'])
print(out_list)


