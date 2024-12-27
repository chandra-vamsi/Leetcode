#2239. Find Closest Number to Zero
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]             #Initializing To first element
        for x in nums:                #Iterating through each element in nums
            if abs(x) < abs(closest): #Comparing Least element
                closest = x           #if found assigning it to a variable       
        if closest < 0 and abs(closest) in nums:# Edge case for values less than 0
            return abs(closest)
        else:
            return closest
