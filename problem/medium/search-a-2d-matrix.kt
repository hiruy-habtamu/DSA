class Solution {
    fun searchMatrix(matrix: Array<IntArray>, target: Int): Boolean {
        var low = 0
        var high = (matrix.size * matrix[0].size)-1

        while(low<=high){
            val mid:Int = low + (high-low)/2
            val row:Int = mid/matrix[0].size
            val col:Int = mid%matrix[0].size 
            
            if(matrix[row][col]==target){
                return true
            }

            if(matrix[row][col]<target){
                low = mid+1
            }
            else{
                high = mid-1
            }
        }
        return false
    }
}