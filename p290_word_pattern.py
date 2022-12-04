class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d1, d2 = {}, {}
        words = s.split()

        if len(words) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            char, word = pattern[i], words[i]
            if ((char in d1 and d1[char] != word) or (word in d2 and d2[word] != char)):
                return False
            else:
                d1[char], d2[word] = word, char
        return True