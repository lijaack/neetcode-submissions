class Solution:
    def foreignDictionary(self, words):
        # Create an adjacency list for every character.
        # adj["a"] contains characters that must come AFTER "a".
        adj = {char: set() for word in words for char in word}

        # Track how many characters must come before each character.
        indegree = {char: 0 for char in adj}

        # Compare every pair of neighboring words.
        # The first different character tells us the ordering.
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            min_length = min(len(word1), len(word2))

            # Invalid case:
            # "abc" cannot come before "ab".
            if (
                len(word1) > len(word2)
                and word1[:min_length] == word2[:min_length]
            ):
                return ""

            # Find the first character where the words differ.
            for j in range(min_length):
                if word1[j] != word2[j]:
                    first_char = word1[j]
                    second_char = word2[j]

                    # first_char must come before second_char.
                    # Use a set so we don't add the same edge twice.
                    if second_char not in adj[first_char]:
                        adj[first_char].add(second_char)
                        indegree[second_char] += 1

                    # Only the FIRST difference matters.
                    break

        # Start with characters that have no prerequisites.
        q = deque(
            char for char in indegree
            if indegree[char] == 0
        )

        result = []

        # Topological Sort (Kahn's Algorithm)
        while q:
            char = q.popleft()
            result.append(char)

            # Removing this character satisfies one prerequisite
            # for each of its neighbors.
            for neighbor in adj[char]:
                indegree[neighbor] -= 1

                # All prerequisites are now satisfied.
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # If we couldn't process every character,
        # there is a cycle → no valid ordering exists.
        if len(result) != len(indegree):
            return ""

        return "".join(result)