class TrieNode:
    def __init__(self):
        # Dictionary stores the next characters connected to this node
        # Example: {"a": TrieNode(), "b": TrieNode()}
        self.children = {}

        # True if a complete word ends at this node
        # Example: inserting "cat" makes the "t" node True
        self.endOfWord = False


class PrefixTree:
    def __init__(self):
        # Start with an empty root node
        # The root doesn't represent a character
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Start at the root
        cur = self.root

        # Go through each character in the word
        for c in word:

            # If this character doesn't exist yet,
            # create a new TrieNode for it
            if c not in cur.children:
                cur.children[c] = TrieNode()

            # Move to the node representing this character
            cur = cur.children[c]

        # We've reached the end of the word,
        # so mark this node as the end of a complete word
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        # Start at the root
        cur = self.root

        # Follow the characters of the word through the Trie
        for c in word:

            # If the character doesn't exist,
            # the word isn't in the Trie
            if c not in cur.children:
                return False

            # Move to the next character/node
            cur = cur.children[c]

        # We found the entire path.
        # But we also need to make sure a COMPLETE word ends here.
        #
        # Example:
        # Insert "apple"
        # search("app") → False
        # because "app" is only a prefix, not a complete word
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        # Start at the root
        cur = self.root

        # Follow each character in the prefix
        for c in prefix:

            # If we can't follow the character,
            # no word starts with this prefix
            if c not in cur.children:
                return False

            # Move to the next node
            cur = cur.children[c]

        # We successfully followed the entire prefix,
        # so at least one word starts with it
        return True