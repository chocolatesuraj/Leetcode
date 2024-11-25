class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def check(src,dest)->int:
            count=0
            for i in range(0,len(src)):
                if(src[i]==dest[i]):
                    count=count+1
            return(len(src)-count)
        print("tesstt")

        wordset=set(wordList)
        if(endWord not in wordset):
            return 0
        words=set()
        temp=set()
        words.add(beginWord)
        print("tesstt")
        ans=0
        while(True):
            print(len(words))
            #print(ans)
            for w in words:
                for w2 in wordset :
                    #if(w2 not in words):
                        
                        if(check(w2,w)==1):
                            #print("w2222",w2,"www",w)
                            temp.add(w2)
                        
            newwords= words | temp
            if(newwords==words):
                return 0
            else:
                words=temp.copy()
            if(endWord in words):
                return ans+2
            wordset=wordset-words
            ans=ans+1


