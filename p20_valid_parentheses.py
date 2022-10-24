class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for x in s:
            if x in '({[':
                stack.append(x)
            else:
                if not stack: 
                    return False
                    # stack was empty ie an unmatched closing parantheses was found
                y = stack.pop()
                combo = y + x
                if combo not in '(){}[]':
                    return False
        # Check if there are any unmatched opening paranthesss left
        if stack:
            return False
        return True