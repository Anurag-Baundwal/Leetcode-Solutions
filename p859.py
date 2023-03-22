class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        idx = []
        if len(s) != len(goal):
            return False

        # if s and goal are same - check for repeated characters
        # if len(set(s)) < len(s) then at least one repeated character exists
        # we can swap this character with itself
        if s == goal:
            return len(set(s)) < len(s)
            
        for i in range(len(goal)):
            if s[i] != goal[i]:
                idx.append(i)
        if len(idx) != 2:
            return False
        return s[idx[0]] == goal[idx[1]] and s[idx[1]] == goal[idx[0]]