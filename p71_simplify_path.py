class Solution:
    def simplifyPath(self, path: str) -> str:
        # keep track of slashes.. if there are more than 1 then reduce them to just 1
        # remove slashes from the end
        
        # run a loop
        # check the char
        # it can be in 'acdef...1234'
        # it can be a slash
        # it can be a dot
        
        ans = []
        for i, char in enumerate(path):
            if char is '/':
                if i == 0:
                    ans.append(char)
                else:
                    
            if char in 'abcdefghijklmnopqrstuvwxyz0123456789':
            
                
                