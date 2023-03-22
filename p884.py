class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = {}
        for word in s1.split():
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
        for word in s2.split():
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
        # print(words.items())
        # return [word for word, count in words.items() if count == 1]
        return [word for word in words if words[word] == 1]