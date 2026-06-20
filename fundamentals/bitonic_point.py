class Solution:
    def findMaximum(self, arr):
        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return arr[left]


sol = Solution()
out = sol.findMaximum([1,5,6,2,1])
print(out)
		