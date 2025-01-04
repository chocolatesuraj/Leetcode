class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=0
        for i in range((len(digits)-1),-1,-1):
            #print(digits[i])
            if(digits[i]<9):
                digits[i]=digits[i]+1
                carry=0
                return digits
            else:
                carry=1
                digits[i]=0
        if(carry==1):
            digits.insert(0,1)
            return digits
            
        
