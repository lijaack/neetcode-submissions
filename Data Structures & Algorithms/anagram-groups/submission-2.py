class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary where each new key automatically starts with an empty list.
        # This lets us do groups[key].append(word) without checking if the key exists.
        groups = defaultdict(list)

        # Go through every word in the input list.
        for word in strs:

            # Create an array of 26 zeros (one spot for each letter a-z).
            # This will store how many times each letter appears.
            letter_count = [0] * 26

            # Look at each letter in the current word.
            for letter in word:

                # ord(letter) converts a character into its ASCII/Unicode number.
                # ord('a') = 97, ord('b') = 98, ..., ord('z') = 122.
                #
                # Subtracting ord('a') turns letters into array indexes:
                # 'a' -> 0
                # 'b' -> 1
                # 'c' -> 2
                # ...
                # 'z' -> 25
                index = ord(letter) - ord('a')

                # Increase the count for this letter.
                letter_count[index] += 1

            # Lists can't be dictionary keys because they can change (mutable).
            # Convert the list to a tuple (immutable) so it can be used as a key.
            #
            # Words with the same letter counts (anagrams) produce the same tuple.
            groups[tuple(letter_count)].append(word)

        # Return only the grouped lists of anagrams.
        return list(groups.values())