class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        l,r = 0,0
        count = defaultdict(int)
        hf = 0
        while r < len(s):
            count[s[r]]+=1
            hf = max(hf,count[s[r]] )
            while r+1-l-hf> k:
                count[s[l]]-=1
                l+=1
            
            res = max(res, r+1-l)
            r+=1
        return res