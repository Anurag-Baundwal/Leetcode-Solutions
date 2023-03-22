class Solution:
    def licenseKeyFormatting(self, s, k):
        s = s.replace("-", "").upper()
        size = len(s)
        s = s[::-1]
        result = ""
        for i in range(size):
            if i % k == 0 and i != 0:
                result += "-"
            result += s[i]
        return result[::-1]
