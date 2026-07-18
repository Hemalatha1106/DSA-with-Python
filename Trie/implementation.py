class Trie:

    def __init__(self):
        self.children={}
        self.flag=False

    def insert(self, word: str) -> None:
        node=self
        for ch in word:
            if ch not in node.children:
                node.children[ch]=Trie()
            node=node.children[ch]
        node.flag=True        

    def search(self, word: str) -> bool:
        node=self
        for ch in word:
            if ch not in node.children:
                return False
            node=node.children[ch]    
        return node.flag        

    def startsWith(self, prefix: str) -> bool:
        node=self
        for ch in prefix:
            if ch not in node.children:
                return False
            node=node.children[ch]    
        return True        
