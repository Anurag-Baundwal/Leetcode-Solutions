class Solution:
    def checkRecord(self, s: str) -> bool:
        d=0
        for i in range(len(s)):
            if s[i]=='A':
                d+=1
            if d==2:
                return False
            if i>=2 and s[i]==s[i-1]==s[i-2]=='L':
                return False
        return True