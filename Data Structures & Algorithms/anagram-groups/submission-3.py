class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary where each new key automatically starts with an empty list.
        # This lets us do groups[key].append(word) without checking if the key exists.
        groups = defaultdict(list)

        for word in strs:
            letter_count = [0] * 26
            for letter in word:
                # ord(letter) converts a character into its ASCII/Unicode number.
                index = ord(letter) - ord('a')
                letter_count[index] += 1
                
            groups[tuple(letter_count)].append(word)

        # Return only the grouped lists of anagrams.
        return list(groups.values())