class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        new_list = []
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if diff in numbers[i+1:]:
                idx1 = numbers.index(numbers[i])
                idx2 = numbers.index(diff)
                new_list = [idx1+1,idx2+1]
                return new_list
            else:
                continue
        
        return []
        


