class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #set all words to a TrieNode
        root = TrieNode()
        curr = root
        for word in words:
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c] 
            curr.word=True
            curr=root

        curr=root
        path = []
        res = set()
        visited=set()
        def dfs(node, i,j):
            #check if letter exist in Tri Node
            #jsut return false if not in
            if (i,j) in visited:
                return
            if board[i][j] not in node.children:
                return
            
            #if its in, we should check surrounding to see if next letter
            node = node.children[board[i][j]]
            path.append(board[i][j])
            visited.add((i,j))
            if node.word:
                res.add("".join(path))
            if i+1 < len(board): 
                dfs(node, i+1, j)
            if i-1 >= 0:
                dfs(node, i-1, j)
            if j+1 < len(board[i]):
                dfs(node, i, j+1)
            if j-1 >= 0:
                dfs(node, i, j-1)
            visited.remove((i,j))
            path.pop()
                    #loop through board
        for i in range(len(board)):
            for j in range(len(board[i])):
                dfs(curr,i,j)
        return list(res)