class Solution:
    def findComplement(self, num):
        # Convert the given number to its binary representation as a string
        binary_num = bin(num)[2:]
        
        # Replace all '0's with '1's and all '1's with '0's in the binary string
        complement = ''
        for digit in binary_num:
            if digit == '0':
                complement += '1'
            else:
                complement += '0'
        
        # Convert the complement binary string back to an integer and return it
        return int(complement, 2)