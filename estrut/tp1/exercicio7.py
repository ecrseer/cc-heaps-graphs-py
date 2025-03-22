class TrieNode:
    """Classe que representa um nó na Trie"""
    def __init__(self):
        self.children = {}  # Dicionário de filhos
        self.is_end_of_word = False  # Indica se é o final de uma palavra

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_palavra(self, palavra):
        node = self.root
        for char in palavra:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def pesquissa(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def list_words(self):
        def _busca_nivel_abaixo(node, prefix, words):
            if node.is_end_of_word:
                words.append(prefix)
            for char, child in node.children.items():
                _busca_nivel_abaixo(child, prefix + char, words)

        words = []
        _busca_nivel_abaixo(self.root, "", words)
        return words


#populando
trie = Trie()
trie.add_palavra("casa")
trie.add_palavra("carro")

print("Listando todas palavras dentro da PRefix Trie:", trie.list_words())

print("A palavra 'casa': está contida na prefix Trie?", trie.pesquissa("casa"))
print("A palavra 'carro': está contida na prefix Trie?", trie.pesquissa("carro"))
print("A palavra 'roxo': está contida na prefix Trie?", trie.pesquissa("roxo"))


trie.add_palavra("caminho")
print("Palavras na Trie:", trie.list_words())