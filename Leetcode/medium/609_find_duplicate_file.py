"""
author: fangren
"""

class Solution(object):
    def split_name_content(self, file):
        ans = file.split('(')
        return ans[0], ans[1][:-1]

    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for path in paths:
            path_split = path.split(' ')
            base_path = path_split[0]
            for file in path_split[1:]:
                file_name, content = self.split_name_content(file)
                if content not in dict:
                    dict[content] = [base_path + '/' + file_name]
                else:
                    dict[content].append(base_path + '/' + file_name)
        ans = []
        for i in dict:
            if len(dict[i]) > 1:
                ans.append(dict[i])
        return ans

paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
solution = Solution()
#print solution.split_name_content('1.txt(abcd)')
print solution.findDuplicate(paths)
