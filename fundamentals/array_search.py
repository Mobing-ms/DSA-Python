class Solution:
    def search(self, arr, x):
        count = 0
        for i in arr:
            if x == i:
                return count
            else:
                count += 1
                
        else:
            return -1
                

sol = Solution()
out = sol.search([1,2,3,4,6,5,7,8],5)
print(out)