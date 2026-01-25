class TimeMap:

    def __init__(self):
        self.hashmap=defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        # print("get",key,timestamp,self.hashmap)
        
        arr=self.hashmap[key]
        if(len(arr)==0):
            return ""
        f=0
        b=len(arr)-1
        m=f
        while(f<b):
            # print(m)
            m=int((f+b)/2)
            if(arr[m][0]>timestamp):
                b=m-1
            elif(arr[m][0]<timestamp):
                f=m+1
            elif(arr[m][0]==timestamp):
                break
        m=max(int((f+b)/2)-1,0)
        while(m+1<len(arr) and arr[m+1][0]<=timestamp):
            # print(arr[m+1][0],timestamp)
            m+=1
        # print(m)
        if(arr[m][0]<=timestamp):
            return arr[m][1]
        return ""
        

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
