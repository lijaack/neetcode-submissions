class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        #sets the letter + for s1 and s2 based on s1 length
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        #how many letters have the same count
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        #left window 0
        l = 0
        #
        #start at the area right after s1 len
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            #right side check 
            index = ord(s2[r]) - ord('a')
            #add the new letter counit
            s2Count[index] += 1
            
            #if new letter ocunt is same as s1 count, it bcomes a match
            if s1Count[index] == s2Count[index]:
                matches += 1
            #if s1count added 1 = s2 count index, then the match is gone. 
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            #check left side. old letter. we're removing count
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            #remove letter so we can make sure the count is same
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            #set new left side
            l += 1
        return matches == 26