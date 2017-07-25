"""
author: fangren
"""
from collections import defaultdict

class Solution(object):
    def repaceWord(self, dict, word):
        found = False
        i = 1
        while not found and i <= len(word):
            short_word = word[:i]
            if short_word in dict[i]:
                found = True
                break
            else:
                i += 1
        if found:
            return short_word
        else:
            return word

    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        if not sentence:
            return ''
        root_dict = defaultdict(list)
        for root in dict:
            root_dict[len(root)].append(root)
        sentence_list = sentence.split(' ')
        for i, word in enumerate(sentence_list):
            word = self.repaceWord(root_dict, word)
            sentence_list[i] = word
        return ' '.join(sentence_list)


solution = Solution()
dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
print solution.replaceWords(dict, sentence)

