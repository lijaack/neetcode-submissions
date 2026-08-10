class Solution:
    def countBits(self, n: int) -> List[int]:
        i=0
        res=[]
        while i <= n:
            count = 0 
            j=i
            while j:
                j= j & (j-1)
                count +=1
            res.append(count)
            i+=1
        return res