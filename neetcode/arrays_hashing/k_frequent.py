from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new_list = []
        count  = list(sorted(Counter(nums).items(),key=lambda x: x[1], reverse = True))
        for i in range(k):
            new_list.append(count[i][0])

        return new_list
        
sol = Solution()
out_list = sol.topKFrequent([1,2,2,3,3,3],2)
print(out_list)