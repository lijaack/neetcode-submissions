class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count all num in nums
        numCount={}
        
        for num in nums:
            numCount[num] = numCount.get(num,0) + 1

        freq =[[] for i in range(len(nums)+1)]
        #then throw them into a bucket according to freq.
        for num, count  in numCount.items():
            freq[count].append(num)
        res=[]
        #we reverse the list of buckets and append the highest freq to res until = k
        for i in range(len(freq) -1, 0 , -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res