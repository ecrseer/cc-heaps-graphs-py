class TrieNo:
    def __init__(self):
        self.filhos = {}
        self.fim_de_palavra = False

class Trie:
    def __init__(self):
        self.raiz = TrieNo()

    def inserir(self, palavra):
        no = self.raiz
        for char in palavra:
            if char not in no.filhos:
                no.filhos[char] = TrieNo()
            no = no.filhos[char]
        no.fim_de_palavra = True

    def buscar(self, palavra):
        no = self.raiz
        for char in palavra:
            if char not in no.filhos:
                return False
            no = no.filhos[char]
        return no.fim_de_palavra

    def comeca_com(self, prefixo):
        no = self.raiz
        for char in prefixo:
            if char not in no.filhos:
                return False
            no = no.filhos[char]
        return True

    def remover(self, palavra):
        def _remover(no, palavra, profundidade):
            if profundidade == len(palavra):
                if not no.fim_de_palavra:
                    return False
                no.fim_de_palavra = False
                return len(no.filhos) == 0

            char = palavra[profundidade]
            if char not in no.filhos:
                return False

            apagar_filho = _remover(no.filhos[char], palavra, profundidade + 1)

            if apagar_filho:
                del no.filhos[char]
                return len(no.filhos) == 0 and not no.fim_de_palavra

            return False

        _remover(self.raiz, palavra, 0)

    def listar_palavras(self):
        def _dfs(no, prefixo, palavras):
            if no.fim_de_palavra:
                palavras.append(prefixo)
            for char, filho in no.filhos.items():
                _dfs(filho, prefixo + char, palavras)

        palavras = []
        _dfs(self.raiz, "", palavras)
        return palavras

# **Testando a Trie**
trie = Trie()

# Inserindo palavras manualmente
palavras = ["carro", "casa", "carteira", "cavalo", "caminho"]
for palavra in palavras:
    trie.inserir(palavra)

print("Palavras na Trie:", trie.listar_palavras())

print("Buscar 'carro':", trie.buscar("carro"))
print("Buscar 'cavalo':", trie.buscar("cavalo"))
print("Buscar 'caminho':", trie.buscar("caminho"))

print("Existe palavra com prefixo 'car'?", trie.comeca_com("car"))

trie.remover("carro")
print("Palavras na Trie após remover 'carro':", trie.listar_palavras())

trie.remover("carteira")
print("Palavras na Trie após remover 'carteira':", trie.listar_palavras())
print("Existe palavra com prefixo 'car'?", trie.comeca_com("car"))
print("Existe palavra com prefixo 'ca'?", trie.comeca_com("ca"))
