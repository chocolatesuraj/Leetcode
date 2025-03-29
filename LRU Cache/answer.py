class Node():
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.hashmap={}
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
        self.cap=capacity
    def printll(self):
        print("priting linked lsit")
        node=self.left.next
        while(node!=None):
            print(node.val)
            node=node.next
            
        
    def remove(self,node):
        # self.printll()
        node.prev.next=node.next
        node.next.prev=node.prev
        # if node.key in self.hashmap:
        self.hashmap.pop(node.key)
    
    def insert(self,key,val):
        newnode=Node(key,val)
        self.right.prev.next=newnode
        newnode.prev=self.right.prev
        self.right.prev=newnode
        newnode.next=self.right
        self.hashmap[key]=newnode
        return newnode

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # print("gettt",key,self.hashmap[key])
        if( key in self.hashmap):
            ret=self.hashmap[key].val
            # print("remove,",self.hashmap[key])
            self.remove(self.hashmap[key])
            self.insert(key,ret)
            return ret
        else:
            return -1
        
        
        

    def put(self, key, value):
        """     
        :type key: int
        :type value: int
        :rtype: None
        """
        if(key in self.hashmap):

            self.remove(self.hashmap[key])
            self.hashmap[key]=self.insert(key,value)
            
        else:
            # print(len(self.hashmap),"   ",self.cap)
            if(len(self.hashmap)>=self.cap):
                self.remove(self.left.next)
                self.hashmap[key]=self.insert(key,value)
            else:
                #key not in hashmap
                self.hashmap[key]=self.insert(key,value)
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
