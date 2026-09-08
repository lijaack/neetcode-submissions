class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0

        # Words we are allowed to transform into.
        words = set(wordList)

        queue = deque([beginWord])
        sequence_length = 0

        while queue:
            sequence_length += 1

            # Process one BFS level at a time.
            for _ in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return sequence_length

                # Try changing each character to a-z.
                for i in range(len(word)):
                    for letter in range(97, 123):
                        new_letter = chr(letter)

                        # Don't replace a character with itself.
                        if new_letter == word[i]:
                            continue

                        neighbor = (
                            word[:i]
                            + new_letter
                            + word[i + 1:]
                        )

                        # If this is a valid word, add it to BFS.
                        if neighbor in words:
                            queue.append(neighbor)

                            # Remove it so we never visit it again.
                            words.remove(neighbor)

        return 0
