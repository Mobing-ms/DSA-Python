class Solution:
    def getAlternates(self, arr):
        new_list = arr[::2]
        
        return new_list

sol = Solution()
out_list = sol.getAlternates([10,20,30,40,50,60,70])

print(out_list)
