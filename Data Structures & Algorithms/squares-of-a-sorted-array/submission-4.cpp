class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector <int> result;
        int left=0;
        int right=nums.size()-1;

        while (left<=right){
            if (abs(nums[left])<abs(nums[right])){
                result.push_back(nums[right]*nums[right]);
                right--;
            }
            else if (abs(nums[left])>abs(nums[right])){
                result.push_back(nums[left]*nums[left]);
                left++;
            }
            else{
                result.push_back(nums[left]*nums[left]);
                left++;

            }
        }
        vector<int> reverse_result(result.rbegin(),result.rend());
        return reverse_result;
    }
};