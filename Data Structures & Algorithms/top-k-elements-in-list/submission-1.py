class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts={}
        #counts = num:how many times seen
        freq=[[] for i in range(len(nums)+1)]
        #for each freq, push the number that have seen that freq into it.
        for num in nums:
            counts[num]=1+ counts.get(num,0)
            # SETS counts {1:3, 2:2, 3:2}
            #
        for key,count in counts.items():
            freq[count].append(key) 
        
        res=[]
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res