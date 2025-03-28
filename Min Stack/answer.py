class MinStack(object):

    def __init__(self):
        self.stack=[]

        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        #lement =[val,min]
        if(self.stack==[]):
            self.stack.append([val,val])
        elif(val<self.stack[-1][1]):
            self.stack.append([val,val])
        else:
            minimum=self.stack[-1][1]
            self.stack.append([val,minimum])
        
        

    def pop(self):
        """
        :rtype: None
        """
        ele=self.stack.pop()
        return ele[0]
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
