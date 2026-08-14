class TrieNode:
    def __init__(self):
        # Array of 26 possible children: a-z
        self.children = [None] * 26

        # Index of the word if a complete word ends here
        # -1 means no complete word ends here
        self.wordIndex = -1

        # Number of words that still exist below this node
        self.refs = 0

    def addWord(self, word, wordIndex):
        curr = self

        # This node now has one more word going through it
        curr.refs += 1

        for char in word:
            index = ord(char) - ord('a')

            # Create the child if it doesn't exist
            if curr.children[index] is None:
                curr.children[index] = TrieNode()

            # Move to the next character
            curr = curr.children[index]

            # Another word passes through this node
            curr.refs += 1

        # Mark this node as the end of a word
        curr.wordIndex = wordIndex


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # ------------------------------------------------
        # Build Trie
        # ------------------------------------------------

        root = TrieNode()

        for i in range(len(words)):
            root.addWord(words[i], i)

        ROWS = len(board)
        COLS = len(board[0])

        result = []

        def getIndex(char):
            return ord(char) - ord('a')

        # ------------------------------------------------
        # DFS / Backtracking
        # ------------------------------------------------

        def dfs(row, col, node):

            # Outside the board
            if row < 0 or row >= ROWS:
                return 0

            if col < 0 or col >= COLS:
                return 0

            # Cell is already being used in this path
            if board[row][col] == '*':
                return 0

            # Current letter doesn't exist in the Trie
            char = board[row][col]
            index = getIndex(char)

            if node.children[index] is None:
                return 0

            # Move to the Trie node for this letter
            previousNode = node
            node = node.children[index]

            # Mark board cell as visited
            board[row][col] = '*'

            found = 0

            # We found a complete word
            if node.wordIndex != -1:
                result.append(words[node.wordIndex])

                # Prevent finding the same word again
                node.wordIndex = -1

                found += 1

            # Explore all 4 directions
            found += dfs(row + 1, col, node)  # down
            found += dfs(row - 1, col, node)  # up
            found += dfs(row, col + 1, node)  # right
            found += dfs(row, col - 1, node)  # left

            # Undo our move / backtrack
            board[row][col] = char

            # Remove words that we've already found
            node.refs -= found

            # If no words remain below this node,
            # remove this Trie branch entirely
            if node.refs == 0:
                previousNode.children[index] = None

            return found

        # ------------------------------------------------
        # Start DFS from every cell
        # ------------------------------------------------

        for row in range(ROWS):
            for col in range(COLS):
                root.refs -= dfs(row, col, root)

        return result