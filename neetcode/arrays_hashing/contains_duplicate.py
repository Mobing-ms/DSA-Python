class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])
        else:
            return False
        
sol = Solution()
out = sol.hasDuplicate([1, 2, 3, 3])
print(out)

