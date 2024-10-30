class Twitter:

    def __init__(self):
        self.folowtable=dict()
        self.tweets=[]
        self.time=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((self.time,userId,tweetId))
        return 

        

    def getNewsFeed(self, userId: int) -> List[int]:
        sol=[]
        length=0
        for i in self.tweets[::-1]:
            time,uid,twid=i
            if(uid==userId or (userId in self.folowtable and uid in self.folowtable[userId])):
                sol.append(twid)
                length=length+1
            if(length==10):
                return sol
            #print(i,"aaaaaaaaaa")
        return sol
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.folowtable:
            self.folowtable[followerId]=set()

        self.folowtable[followerId].add(followeeId)
            
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.folowtable:
            self.folowtable[followerId].remove(followeeId)
        return 
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
