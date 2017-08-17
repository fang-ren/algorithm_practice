"""
author: Fang Ren (SSRL)

3/14/2017
"""

matrix = [['O', 'C', 'H'], ['A', 'S', 'T'], ['T', 'R', 'Q']]

import numpy as np

word_dict = ['CASH', 'STAR', 'START', 'COACH']


def finding_neighbor((i,j)):
    neighbors = [(i-1, j-1), (i-1, j), (i, j-1), (i+1, j), (i, j+1), (i+1, j+1), (i+1, j-1), (i-1, j+1)]
    return neighbors

# a = finding_neighbor((2,3))
# print a

def main(matrix, word_dict):
    matrix = np.array(matrix)
    dim = matrix.shape
    found = []
    # print dim
    for i in range(dim[0]):
        for j in range(dim[1]):
            longest_words = [[(i,j)]]
            found += longest_words
            # print longest_words, found
            while longest_words:
                next = []
                for current_word in longest_words:
                    last_letter = current_word[-1]
                    neighbors = finding_neighbor(last_letter)
                    for neighbor in neighbors:
                        if neighbor[0] in np.arange(0,dim[0]) and neighbor[1] in np.arange(0,dim[1]):
                            if neighbor not in current_word:
                                new_word = current_word + [neighbor]
                                found.append(new_word)
                                next.append(new_word)
                longest_words = next
    # print found

    ans = []
    for word_found in found:
        result = ''
        # print word_found
        for index in word_found:
            result += matrix[index]

            # print result
        if result in word_dict:
            ans.append(result)
    return ans

ans = main(matrix, word_dict)
print ans

for i in ans:
    print i