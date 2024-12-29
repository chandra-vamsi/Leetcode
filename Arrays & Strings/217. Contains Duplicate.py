#217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/description/
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset=set()            #Initializing Hashset as set doesnt contain anyduplicates
        for x in nums:           #Going through each element in list
            if x in hashset:     #if it exsist 
                return True      #return true 
            hashset.add(x)       #else add it to hashset
        return False             #no Element found return False
