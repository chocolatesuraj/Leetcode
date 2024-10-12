class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if(digits==""):
            return []
        translations=[["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u", "v"],["w","x","y","z"]]
        res=[]
        num=int(digits[0])-2
        for i in translations[num]:
            res.append(i) 

        

        for numchar in digits[1:]:
            num=int(numchar)-2
            tempres=[]
            for i in translations[num]:
                for ele in res:
                    tempres.append(ele+i)

            res=tempres
        
        return res

            
        
