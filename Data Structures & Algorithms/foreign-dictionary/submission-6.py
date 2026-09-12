class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}
        indegree = {char:0 for char in adj}

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            min_len = min(len(word2), len(word1))

            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""
            for j in range(min_len):
                if word1[j] != word2[j]:
                    if word2[j] not in adj[word1[j]]:
                        adj[word1[j]].add(word2[j])
                        indegree[word2[j]] +=1
                    break
        q=deque(char for char in indegree if indegree[char] == 0)
        res=[]
        while q:
            char = q.popleft()
            res.append(char)
            for neighbor in adj[char]:
                indegree[neighbor] -=1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        if len(res) != len(adj):
            return ""
        return "".join(res)