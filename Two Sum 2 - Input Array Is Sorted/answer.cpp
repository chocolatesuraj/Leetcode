class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int f=0;
        int sum =0;
        std::vector<int> ans={0,0};
        int b=numbers.size()-1;
        while(f<b){
            sum=numbers[f]+numbers[b];
            if(sum==target)
                {ans={f+1,b+1};
                return ans ;}
            else if(sum<target){
                f++;
            }
            else{
                b--;
            }
            
        }
        return ans;
        
    }
};
