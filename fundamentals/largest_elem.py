#finding the largest element from a list

class Solution:
    def largest_element(self,arr):
        if len(arr) >= 2:
            temp = arr[0]
            for i in range(len(arr)):
                if (temp <= arr[i]):
                    temp = arr[i]
            return temp

        elif len(arr) == 1:
            temp = arr
            return int(temp[0])

        else:
            return None

sol = Solution()
largest = sol.largest_element([10,1,2,3])
print(largest)