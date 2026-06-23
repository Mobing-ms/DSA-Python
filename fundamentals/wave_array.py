class Solution:
    def sortInWave(self, arr):
        temp = 0
        for i in range(len(arr)):
            if len(arr) % 2 == 1:
                if i != len(arr) - 1:
                    if i % 2 == 1:
                        temp = arr[i]
                        arr[i] = arr[i - 1]
                        arr[i - 1] = temp
                        continue
                    else :
                        continue
                else:
                    break
            else:
                if i % 2 == 1:
                        temp = arr[i]
                        arr[i] = arr[i - 1]
                        arr[i - 1] = temp
                        continue
                else :
                    continue

        return arr

sol = Solution()
out_list = sol.sortInWave([2, 4, 7, 8, 9, 10])
print(out_list)
            
            
        
