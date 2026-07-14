#include <vector>
#include <algorithm>
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        
        vector<vector<int>> answer;
        
        int left;
        int right;

        sort(nums.begin(), nums.end());

        for (int i=0;i<nums.size();i++){
            left=i+1;
            right=nums.size()-1;

            while (left<right){

                if (nums[i]+nums[left]+nums[right]<0){
                    left++;
                }
                else if (nums[i]+nums[left]+nums[right]>0){
                    right--;
                }
                else{
                    vector<int> triplet = {nums[i], nums[left], nums[right]};

                    if (find(answer.begin(), answer.end(), triplet) == answer.end()) {
                        answer.push_back(triplet);
                    }
                    left++;
                    right--;
                }

            }
        }
        return answer;
    }
    
};
