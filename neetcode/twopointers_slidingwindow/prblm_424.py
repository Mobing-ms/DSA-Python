class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        l,r = 0,1 
        new_list = list(s)
        index_store = []
        index_store.append(-1)
        countA = s.count('A')
        countB = s.count('B')
        #function to check the maxlen after soting the k into the new_string
        def maxLength(req_char,s):
            maxlen,temp = 0,0
            if req_char == 'A':
                for i in range(len(s)):
                    if s[i] == 'A':
                        temp += 1
                    else:
                        maxlen = max(maxlen,temp)
                        temp = 0
                        continue
                return maxlen


        maxfreq = max(countA,countB)   
        if maxfreq == countA:
            req_char = 'A'
        else:
            req_char = 'B'

        #dealing if k == 0..that function shld work for k = 0
        if k == 0:
            maxLength(req_char,s)

        #if k > 0 then we should make the new  optimal string for longer repeater character    
        else:
            for i in range(len(s)):
                if req_char == 'A':
                    if s[i] == 'A':
                        continue
                    else:
                        index_store.append(i)
                else:
                    if s[i] == 'B':
                        continue
                    else:
                        index_store.append(i)
            len_index_store = len(index_store)
            index_store2 = []
            while k != 0:
                while r < len_index_store:
                    index_store2.append(abs(index_store[l] - index_store[r]))
                    l+=1
                    r+=1
                idx = index_store2.index(max(index_store2))
                index_store2[idx] = 0
                new_list[index_store[idx+1]] = req_char
            s = "".join(new_list) 
            maxLength(req_char,s)
            """
        maxf = 0
        res = 0
        count  = {}
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            maxf = max(count.values())

            while (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res,r-l+1)
        return res      