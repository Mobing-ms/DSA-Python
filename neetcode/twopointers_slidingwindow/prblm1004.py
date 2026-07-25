class Solution:
    def longestOnes(self, nums: List[int], k: int):
        """
        res = 0
        count = {}
        l = 0

        for r in range(len(nums)):
            count[nums[r]] = 1 + count.get(nums[r], 0)

            if (r - l + 1) - count.get(1, 0) > k:
                count[nums[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
        """
        
        zeroc = 0
        l = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroc += 1
            if zeroc > k:
                if nums[l] == 0:
                    zeroc -= 1
                l += 1
        return len(nums) - l
            