class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        n = len(arr)
        if(n<3):
            return False
        i = arr.index(max(arr))
        if(i==0 or i==n-1):
            return False
        for j in range(i,0,-1):
            if(arr[j]>arr[j-1]):
                continue
            else:
                return False
        for j in range(i,n-1):
            if(arr[j]>arr[j+1]):
                continue
            else:
                return False

        return True