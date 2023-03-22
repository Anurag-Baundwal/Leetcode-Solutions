class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word == word.upper() or word == word.capitalize() or word == word.lower()
        # return word.isupper() or word.islower() or word.istitle()