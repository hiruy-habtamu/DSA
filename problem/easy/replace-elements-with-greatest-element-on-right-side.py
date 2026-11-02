class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        n = len(arr)
        maxRight=-1
        for i in range(n-1,-1,-1):
            curr = arr[i]
            arr[i]=maxRight
            if(curr>maxRight):
                maxRight = curr
        return arr