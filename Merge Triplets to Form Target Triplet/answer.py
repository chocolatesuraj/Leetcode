class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        one=False
        two=False
        three=False
        for tri in triplets:
            if(tri[1]==target[1] and tri[2]<=target[2] and tri[0]<=target[0]):
                one=True
            if(tri[2]==target[2] and tri[1]<=target[1] and tri[0]<=target[0]):
                two=True
            if(tri[0]==target[0] and tri[2]<=target[2] and tri[1]<=target[1]):
                three=True
        if(one and two and three):
            return True 
        return False
        
