#-*- coding: utf-8 -*-


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []

        total_len = len(words) * len(words[0])
        if total_len > len(s):
            return []

        res = []
        for i in range(len(s)):
            if total_len > (len(s) - i):
                break
            else:
                if self.inner_find(i, s, words, []):
                    res.append(i)

        return res

    def inner_find(self, index, s, words, has_word_index):
        if len(has_word_index) == len(words):
            return True

        for i, word in enumerate(words):
            if i not in has_word_index:
                if s[index:len(word) + index] == word:
                    has_word_index.append(i)
                    index = len(word) + index
                    return self.inner_find(index, s, words, has_word_index)

        return False


print(Solution().findSubstring("abababab",["a","b","a"]))
