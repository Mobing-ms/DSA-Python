class Solution(object):
    def findDuplicate(self, nums):
        counts = Counter(nums)
        for key,count in counts.items():
            if count > 1:
                value = key
            else:
                continue
        return value