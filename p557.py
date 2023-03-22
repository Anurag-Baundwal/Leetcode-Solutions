class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into a list of words using the space character as the separator
        words = s.split(' ')

        # Use a list comprehension to reverse each word in the list
        reversed_words = [w[::-1] for w in words]

        # Join the reversed words back together with a space character between them
        return ' '.join(reversed_words)
