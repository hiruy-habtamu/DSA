class Solution {
    fun findTheWinner(n: Int, k: Int): Int {
        val list = MutableList(n){
            index-> index+1
        }
        var del = (k-1)%n

        while(list.size>1){
            list.removeAt(del)
            del = (del +(k-1))%list.size
        }

        return list[0]
    }
}