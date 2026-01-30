class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        b, f = -1, len(people) - 1
        people.sort()
        count=0
        while(b<f):
            s=people[f]
            # print(f)
            if(s+people[b+1]<=limit and b+1!=f):
                s=s+people[b+1]
                b+=1
                # print(b-1,f)
            f-=1
            count+=1
        return count
