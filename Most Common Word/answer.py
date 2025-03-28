class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        hashmap={}
        maxnum=0
        maxstr=""
        paragraph=paragraph.replace(","," ")
        # print(paragraph)
        words=paragraph.split(" ")
        for i,word in enumerate(words):
            if(len(word)>=1):
                words[i]=word.lower()
                for y in word:
                    if not ( ord("a")<=ord(y)<=ord("z")  or ord("A")<=ord(y)<=ord("Z")):
                        print("removing",y)
                        words[i]=words[i].strip(y)
                print(words[i])
                if(words[i] in banned):
                    print("skiping banned word")
                    continue 
                elif(words[i] in hashmap):
                    hashmap[words[i]]=hashmap[words[i]]+1
                else:
                    hashmap[words[i]]=1
                if(hashmap[words[i]]>maxnum):
                    maxnum=hashmap[words[i]]
                    maxstr=words[i]

        # print(hashmap)  
        # print(words)
        return maxstr
        
