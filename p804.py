class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # Morse code mapping for each letter
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
                 "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]
        
        # Set to store unique Morse code transformations
        unique_transformations = set()
        
        for word in words:
            # Map each letter in the word to its Morse code sequence
            morse_code = ''.join([morse[ord(letter) - ord('a')] for letter in word])
            
            # Add the Morse code transformation to the set
            unique_transformations.add(morse_code)
        
        # Return the number of unique Morse code transformations
        return len(unique_transformations)