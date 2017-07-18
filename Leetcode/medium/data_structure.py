"""
author: fangren
"""

class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = []

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if word not in self.dict:
            self.dict.append(word)


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        for existing_word in self.dict:
            if len(existing_word) != len(word):
                continue
            matching = True
            for i in range(len(word)):
                if word[i] == '.':
                    continue
                if word[i] != existing_word[i]:
                    matching = False
                    break
            if matching == True:
                return True
        return False


dictionary = WordDictionary()
a = dictionary.dict
dictionary.addWord("bad")
dictionary.addWord("dad")
dictionary.addWord("mad")
print dictionary.dict
print dictionary.search('mat')