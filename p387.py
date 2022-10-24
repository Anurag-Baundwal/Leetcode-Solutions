# 387. First Unique Character in a String

class Solution:
    # My solution:
    def firstUniqChar(self, s: str) -> int:
        abc = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 
                    'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
                    'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
                    'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        
        for x in s:
            abc[x] = abc[x] + 1
        #print(abc)
        
        for i in range(len(s)):
            if abc[s[i]] == 1: # this means that this letter appears only once in the entire string
                return i
            
        return -1
        #####

    # Soltution from discussions section
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for l in s:
            if l not in d: d[l] = 1
            else: d[l] += 1
        # for l in s:
        #    d[l] += 1
        # this won't work because d[l] might not exist and hence we can't access it
        # for example d['m'] won't exist in case of "leetcode"
        # this would give us KeyError
        index = -1
        for i in range(len(s)):
            if d[s[i]] == 1:
                index = i
                break
        
        return index