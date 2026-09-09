class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0

        words = set(wordList)
        letters = "abcdefghijklmnopqrstuvwxyz"

        q = deque([beginWord])
        sequence_len = 0
        while q:
            sequence_len += 1
            #loop through q with len(q)
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return sequence_len
                for i in range(len(word)):
                    for letter in letters:
                        if letter == word[i]:
                            continue
                        neighbor = word[:i] + letter + word[i+1:]

                        if neighbor in words:
                            q.append(neighbor)
                            words.remove(neighbor)
        
        return 0