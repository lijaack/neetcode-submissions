class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0

        word_length = len(beginWord)
        word_set = set(wordList)

        # BFS from both ends.
        begin_queue = deque([beginWord])
        end_queue = deque([endWord])

        # Distance from each starting point.
        distance_from_begin = {beginWord: 1}
        distance_from_end = {endWord: 1}

        while begin_queue and end_queue:

            # Always expand the smaller side.
            if len(begin_queue) > len(end_queue):
                begin_queue, end_queue = end_queue, begin_queue
                distance_from_begin, distance_from_end = (
                    distance_from_end,
                    distance_from_begin
                )

            # Process one BFS level.
            for _ in range(len(begin_queue)):
                word = begin_queue.popleft()
                steps = distance_from_begin[word]

                # Try changing each character to a-z.
                for i in range(word_length):
                    for letter in range(97, 123):
                        new_letter = chr(letter)

                        if new_letter == word[i]:
                            continue

                        neighbor = (
                            word[:i]
                            + new_letter
                            + word[i + 1:]
                        )

                        if neighbor not in word_set:
                            continue

                        # The two BFS searches have met.
                        if neighbor in distance_from_end:
                            return steps + distance_from_end[neighbor]

                        # Haven't visited this word from this side yet.
                        if neighbor not in distance_from_begin:
                            distance_from_begin[neighbor] = steps + 1
                            begin_queue.append(neighbor)

        return 0
