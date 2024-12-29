# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j=0,0                                 #initializing two pointers to take compare
        while i<len(s) and j<len(t):            # Looping Through strings 
            if s[i]==t[j]:                      # If equal movie the above pointer(The string that needs to be substring) 
                i+=1
            j+=1                                #else move the pointer of Second string 
        return i==len(s)                        #at last comparing pointer to length of s if equal that would be a substring
        
