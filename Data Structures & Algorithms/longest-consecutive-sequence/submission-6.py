class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest= 0
        #we need to loop through the numbers
        for num in numset:
            #if its in numset, currLength = 1
            currLen = 1

            #if number-1 is numset, we can skip because we already checked
            if num-1 in numset:
                continue
            # if its not in numset, we can start a loop to check the following numbers
            while num+currLen in numset:
            #while the following numbers in numset, we can add currlength+1
                currLen+=1
            #exit while loop once the num+currlength is not in numset

            longest = max(longest,currLen)



        return longest