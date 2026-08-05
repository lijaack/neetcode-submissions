class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=defaultdict(list)
        #loop through each word
        #tuple use array of 26[0] for letters. up the letter count
        for word in strs:
            letters = [0]*26
            for letter in word:
                letters[ord(letter)-ord('a')] += 1
            groups[tuple(letters)].append(word)
        
        #create a list(tuple.values())
        return list(groups.values())