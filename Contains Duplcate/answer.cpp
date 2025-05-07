class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::unordered_set<int> dup;
        for(int i=0; i<nums.size(); i++){
            if(dup.find(nums[i])!=dup.end()){
                return true;
            }
            else{
                dup.insert(nums[i]);

            }

        }
        return false;
    }
    
};
