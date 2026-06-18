class Solution:
    def firstRepeated(self,arr):
        temp = arr[0]
        count = 0
        for i in range(len(arr)):
            if arr.count(arr[i]) >= 2:
                return (count + 1)
            else:
                count+=1
                continue
        else:
            return -1

sol = Solution()
out = sol.firstRepeated([1,5,3,4,3,5,6])
print(out)
