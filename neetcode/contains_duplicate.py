class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = 0
        for i in range(len(nums)):
            if nums.count(nums[i]) >= 2:
                return True  
        else:
            return False
        
sol = Solution()
out = sol.hasDuplicate([1, 2, 3, 3])
print(out)

