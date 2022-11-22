class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = 0
        for i, char in enumerate(a):
            sum += (int(char)) * (2**(len(a)-i-1)) # eg a = "11" -> len = 2 -> 2**2 + 2**1
        for i, char in enumerate(b):
            sum += (int(char)) * (2**(len(b)-i-1)) # eg a = "11" -> len = 2 -> 2**2 + 2**1
        
        binary = ""
        if sum == 0: binary = "0"
        while(sum > 0):
            digit = str(sum%2)
            binary = digit + binary
            sum = sum // 2
        return binary
        