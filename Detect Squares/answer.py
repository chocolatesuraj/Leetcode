class DetectSquares:

    def __init__(self):
        self.dic=dict()

    def add(self, point: List[int]) -> None:
        a=point[0]
        b=point[1]
        if((a,b) in self.dic):
            self.dic[(a,b)]=self.dic[(a,b)]+1
        else:
            self.dic[(a,b)]=1

        

    def count(self, point: List[int]) -> int:
        num=0
        key3=point[0]
        key4=point[1]
        #print("countt")
        for key1,key2 in self.dic:
            #print(key1,key2,"aa",abs(key2-key4),abs(key1-key3))
            

            if( (abs(key2-key4)==abs(key1-key3)) and (abs(key2-key4)>0 )):
                l=abs(key2-key4)
                #print("llll",l,(key1+l,key1),(key3-l,key4))
                #print("llll",l,(key1-l,key2),(key3+l,key4))
                if(  ((key1+l,key2) in self.dic) and ((key3-l,key4) in self.dic ) and (abs(key1+l-key3+l)==abs(key2-key4)) ):
                    #print("kkkkk")
                    num=num+(self.dic[(key1,key2)] * self.dic[(key1+l,key2)]  * self.dic[(key3-l,key4)]  )
                if(  ((key1-l,key2) in self.dic) and ((key3+l,key4) in self.dic ) and (abs(key1-l-key3-l)==abs(key2-key4))   ):
                    #print("kkkkk")
                    num=num+(self.dic[(key1,key2)] * self.dic[(key1-l,key2)]  * self.dic[(key3+l,key4)]   )
                    
        return num
                        
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
