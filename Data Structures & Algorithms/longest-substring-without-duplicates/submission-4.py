class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        seen={}
        longest = 1
        left=0
        

        #loop through, and check each letter if its indexed inside the dict
        for i,curr in enumerate(s):
        
            #if it is inside dict, we need to that the index position as new left
            if s[i] in seen and seen[s[i]]>=left:
                left = seen[s[i]]+1
            #if its not inside dict, we can add it to the dict and add to maxlen
                        #maxlen should be i - left
            else:
                longest = max(longest,i-left+1)
            seen[s[i]] = i

        return longest

