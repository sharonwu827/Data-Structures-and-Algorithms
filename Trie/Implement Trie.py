class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNodd()

    def charToIndex(self, ch):
        '''
        :param ch: use only 'a' through 'z' and lower case
        :return: Converts key current character into index
        '''
        return ord(ch) - ord('a')

    def insert(self, key):




