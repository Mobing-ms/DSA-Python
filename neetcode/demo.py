class Solution:

    def encode(self, strs: List[str]) -> str:
        new_strs = "#".join(strs)
        return new_strs

    def decode(self, strs: str) -> List[str]:
        new_list = strs.split('#')
        return new_list
        

sol = Solution()
out1 = sol.encode(['apple','orange','pineapple','watermelon'])
out2 = sol.decode('apple#orange#pineapple#watermelon')
print(out1)
print(out2)