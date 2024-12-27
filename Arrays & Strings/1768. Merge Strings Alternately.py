#1768. Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        z="" #initializing a blank string to append
        i=0 #a pointer to point index
        while (i<len(word1) or i<len(word2)): #looping till the end of each word
            if(i<len(word1)):
                z=z+word1[i] #adding single letter of first word
            if(i<len(word2)):
                z=z+word2[i] #adding the character of alternative word
            i=i+1
        return z
