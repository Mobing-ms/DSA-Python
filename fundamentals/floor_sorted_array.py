class Solution:
    def findFloor(self, arr, x):
        left,right = 0,len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] <= x:
                left = mid + 1

            if arr[mid] > x:
                right = mid - 1

        return left - 1

sol = Solution()
out = sol.findFloor([1,2,8,10,10,12,19],0)
print("Index is: " ,out)