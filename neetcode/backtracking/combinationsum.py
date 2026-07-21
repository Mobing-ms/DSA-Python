class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        def backtrack(idx,path,new_sum):
            if idx == n or new_sum > target:
                return
            if new_sum == target:
                result.append(path[:])
                return 
            

            path.append(candidates[idx])
            backtrack(idx,path,new_sum + candidates[idx])
            path.pop()
            backtrack(idx + 1,path,new_sum)

        backtrack(0,[],0)
        return result

        

            