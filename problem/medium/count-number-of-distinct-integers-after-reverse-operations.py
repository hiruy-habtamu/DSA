class Solution:
    def reverseNum(self,num:int)-> int:
        reverse = 0
        while num>0:
            reverse = (reverse *10) + num%10
            num//=10
        return reverse

    def countDistinctIntegers(self, nums: list[int]) -> int:
        numSet = set(nums)
        n = len(nums)
        for i in range(n):
            numSet.add(self.reverseNum(nums[i]))
        return len(numSet)