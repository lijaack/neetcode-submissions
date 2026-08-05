class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary where every new key automatically starts as an empty list
        groups = defaultdict(list)

        for word in strs:
            letter_count = [0] * 26

            for letter in word:
                index = ord(letter) - ord('a')
                letter_count[index] += 1

            groups[tuple(letter_count)].append(word)

        return list(groups.values())