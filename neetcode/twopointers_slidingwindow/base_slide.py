class Solution:
    def maxSum(self,nums,k):
        temp = 0
        n = len(nums)
        l,r = 0,k-2

        while r <= n-1:
            r+=1
            temp = max(temp,sum(nums[l:r+1]))
            l+=1
        return temp
    
sol = Solution()
out = sol.maxSum([-1, 2, 3, 3, 4, 5, -1],5)
print(out)


