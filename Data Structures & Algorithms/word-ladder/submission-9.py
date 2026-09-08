class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # If the target word isn't in the list, there is no possible path.
        if endWord not in wordList or beginWord == endWord:
            return 0

        # Map each wildcard pattern to all words that match it.
        # Example:
        # "hot" -> "*ot", "h*t", "ho*"
        #
        # Words sharing a pattern differ by exactly one character.
        nei = collections.defaultdict(list)

        # Build the wildcard pattern map.
        for word in wordList:
            for j in range(len(word)):

                # Replace one character with "*".
                # Example: "hot" -> "*ot", "h*t", "ho*"
                pattern = word[:j] + "*" + word[j + 1:]

                # Store the word under this pattern.
                nei[pattern].append(word)

        # Track words we've already discovered.
        # This prevents visiting the same word repeatedly.
        visit = set([beginWord])

        # Standard BFS queue.
        q = deque([beginWord])

        # beginWord counts as sequence length 1.
        res = 1

        while q:

            # Process every word at the current BFS level
            # before moving to the next level.
            for i in range(len(q)):

                word = q.popleft()

                # We reached the target.
                if word == endWord:
                    return res

                # Generate all wildcard patterns for this word.
                for j in range(len(word)):

                    # Example: "hot" -> "*ot", "h*t", "ho*"
                    pattern = word[:j] + "*" + word[j + 1:]

                    # Every word sharing this pattern is a neighbor.
                    for neiWord in nei[pattern]:

                        # Only visit each word once.
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)

            # Finished this entire level.
            # Move to the next sequence length.
            res += 1

        # No transformation sequence exists.
        return 0
