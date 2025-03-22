class TrieNode:
    """Classe que representa um nó na Trie"""
    def __init__(self):
        self.children = {}  # Dicionário de filhos
        self.is_end_of_word = False  # Indica se é o final de uma palavra

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, palavra):
        node = self.root
        for char in palavra:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word





#populando
trie = Trie()
trie.insert("casa")
trie.insert("carro")

print("Listando todas palavras dentro da PRefix Trie:", trie.list_words())

print("A palavra 'casa': está contida na prefix Trie?", trie.search("casa"))
print("A palavra 'carro': está contida na prefix Trie?", trie.search("carro"))
print("A palavra 'roxo': está contida na prefix Trie?", trie.search("roxo"))


trie.insert("caminho")
print("Palavras na Trie:", trie.list_words())