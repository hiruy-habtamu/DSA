class Solution {
    fun applyOperations(nums: IntArray): IntArray {
        var lastZeroIndex = 0
        for(i in 0..<nums.size-1){
            if(nums[i]==nums[i+1]){
                nums[i]*=2
                nums[i+1]=0
            }
        }
        for(i in nums.indices){
            if(nums[i]!=0){
                val temp = nums[i]
                nums[i] = nums[lastZeroIndex]
                nums[lastZeroIndex] = temp
                lastZeroIndex++
            }
        }
        return nums
    }
}