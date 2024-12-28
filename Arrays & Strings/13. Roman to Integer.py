#13. Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}   #initializing dictionary with the values        
        summ=0                                                   #initializing variable to sum to track   
        i=0                                                      #initializing variable to track of iteration
        n=len(s)                                                 #initializing n to length
        while i<n:                                               #Looping through each string 
            if i<n-1 and d[s[i]]<d[s[i+1]]:                      #Comparing each character with next character 
                summ+=d[s[i+1]]-d[s[i]]                          #if its less than the next character will add the subtraction and moving two characters
                i+=2
            else:
                summ+=d[s[i]]                                    #Else adding the element and adding 1 to i 
                i+=1                                             
        return summ
