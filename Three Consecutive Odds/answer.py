class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        i=0
        while(i<len(arr)-2):
            if(arr[i]%2!=0):
                if(arr[i+1]%2!=0):
                    if(arr[i+2]%2!=0):
                        return True
                    else:
                        i+=3
                else:
                    i+=2
            else:
                i+=1
        return False
