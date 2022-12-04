class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # initialise all the bits to 0
        # one number is missing so we actually need n+1 bits 
        bits = [0 for i in range(len(nums)+1)] 
        
        # set bits by looping through nums
        # we only need to loop once
        for i in nums:
            bits[i] = 1
        
        # now check the bits to find out which number is missing
        # eg: if 3 was missing -> bits[3] would be 0 -> i would be equal to 3 -> we return 3        
        for i, b in enumerate(bits):
            if b == 0:
                return i