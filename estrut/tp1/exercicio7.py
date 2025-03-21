class TrieNode:
    """Classe que representa um nó na Trie"""

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    """Classe que representa a Trie"""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
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


    def delete(self, word):

        def _delete(node, word, depth):
            if depth == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0

            char = word[depth]
            if char not in node.children:
                return False

            should_delete_child = _delete(node.children[char], word, depth + 1)

            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word

            return False

        _delete(self.root, word, 0)

    def list_words(self):

        def _dfs(node, prefix, words):
            if node.is_end_of_word:
                words.append(prefix)
            for char, child in node.children.items():
                _dfs(child, prefix + char, words)

        words = []
        _dfs(self.root, "", words)
        return words


trie = Trie()
trie.insert("carro")
trie.insert("casa")
trie.insert("carteira")
trie.insert("cavalo")

print("Palavras na Trie:", trie.list_words())

print("Buscar 'carro':", trie.search("carro"))
print("Buscar 'cavalo':", trie.search("cavalo"))
print("Buscar 'caminho':", trie.search("caminho"))

trie.insert("caminho")
print("Palavras na Trie:", trie.list_words())
print("Buscar 'caminho':", trie.search("caminho"))

trie.delete("carro")
print("Palavras na Trie:", trie.list_words())

trie.delete("carteira")
print("Palavras na Trie:", trie.list_words())