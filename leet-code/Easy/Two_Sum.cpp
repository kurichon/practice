class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        int sum = 0;
        unordered_map<int,int> unorderedMap;
        for(int i = 0; i < nums.size() ;i++) 
        {
            int complement = target - nums[i];
            if (unorderedMap.find(complement) != unorderedMap.end())
            {
               return {unorderedMap[complement],i};
            }

            unorderedMap[nums[i]] = i;
        }
        return {};
    }
};
