class treeNode:
    def __init__(self):
        self.children = {}
        self.endofWord = False

class Trie:

    def __init__(self):
        self.root = treeNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] =  treeNode()
                curr = curr.children[char]
        
        curr.endofWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for char in word:
            if char not in curr.children:
                return  False
            curr = curr.children[char]
        return curr.endofWord 

        

    def startsWith(self, prefix: str) -> bool:
        
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return  False
            curr = curr.children[char]
        
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)