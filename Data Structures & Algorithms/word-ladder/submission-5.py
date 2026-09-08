class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0

        num_words = len(wordList)
        word_length = len(wordList[0])

        # Give each word an index so we can build a graph.
        word_to_index = {}

        for i in range(num_words):
            word_to_index[wordList[i]] = i

        # Adjacency list.
        # adj[i] = all words that differ from wordList[i] by one letter.
        adj = [[] for _ in range(num_words)]

        # Compare every pair of words.
        # If they differ by exactly one character, connect them.
        for i in range(num_words):
            for j in range(i + 1, num_words):
                differences = 0

                for k in range(word_length):
                    if wordList[i][k] != wordList[j][k]:
                        differences += 1

                if differences == 1:
                    adj[i].append(j)
                    adj[j].append(i)

        # Start BFS with all words that are one letter away from beginWord.
        queue = deque()
        visited = set()

        for i in range(word_length):
            for letter in range(97, 123):  # a through z
                if chr(letter) == beginWord[i]:
                    continue

                new_word = (
                    beginWord[:i]
                    + chr(letter)
                    + beginWord[i + 1:]
                )

                if new_word in word_to_index:
                    word_index = word_to_index[new_word]

                    if word_index not in visited:
                        queue.append(word_index)
                        visited.add(word_index)

        # beginWord counts as the first word in the sequence.
        sequence_length = 1

        while queue:
            sequence_length += 1

            # Process one BFS level at a time.
            for _ in range(len(queue)):
                current = queue.popleft()

                # We reached the target word.
                if wordList[current] == endWord:
                    return sequence_length

                for neighbor in adj[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        return 0
