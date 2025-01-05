class Solution:
    def countAndSay(self, n: int) -> str:
        sys.set_int_max_str_digits(6400)
        '''
        1
        11
        21
        1211
        111221
        312211
        '''
        if(n==1):
            return "1"
        num=self.countAndSay(n-1)
        ans=0
        num=str(num)
        oldnum=num[0]
        #print(oldnum,num)
        count=0
        for i in num:
            if(i==oldnum):
                count+=1
            else:
                ans=(ans*10)+count
                ans=(ans*10)+int(oldnum)
                oldnum=i
                count=1
        ans=(ans*10)+count
        ans=(ans*10)+int(oldnum)
        
        #print("numm",num,"x",ans)
        return str(ans)

