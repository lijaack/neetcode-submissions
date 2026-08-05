class Solution:
    def isPalindrome(self, s: str) -> bool:
        #left starts at index 0
        left = 0
        #right starts at last index
        right = len(s) - 1

        # stop when left = past mid point
        while left < right:
            #+1 until its a number or letter and not some random char
            while left < right and not s[left].isalnum():
                left += 1
            #-1 from right until its a number or letter
            while left < right and not s[right].isalnum():
                right -= 1
            
            #compare each 
            if s[left].lower() != s[right].lower():
                return False

            #skipped the previous +- so we have to do it here. 
            left += 1
            right -= 1

        return True