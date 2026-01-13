class Node:
    def __init__(self):
        self.word=False
        self.children=[None]*26

class WordDictionary:

    def __init__(self):
       self.trie=Node()
       
    def addWord(self, word: str) -> None:
        # print("add",word)
        head=self.trie
        for c in word:
            pos=ord(c)-ord("a")
            # print(c,pos)
            if head.children[pos]==None:
                head.children[pos]=Node()
            head=head.children[pos]
        # print(head)
        head.word=True
    
        
    def search(self, word: str) -> bool:
        # print("search",word)

        def func(node,pos):
            if(pos == len(word)):
                # print("end",word,node.word)
                if(node.word==True):
                    return True
                return False
            # print("func",word,pos)
            if(word[pos]=="."):
                ans=False
                for i in range(0,26):
                    # print(word[i],ord(word[i])-ord("a"))
                    # print(i)
                    child=node.children[i]
                    # print("loop",child)
                    if(child!=None):
                        ans=ans or func(child,pos+1)
                        if(ans==True):
                            return True
                return ans 



            else: # not "."
                child=node.children[ord(word[pos]) - ord("a")]
                if(child!=None):
                    return func(child,pos+1)
                else:
                    return False


            
        return func(self.trie,0)



        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
