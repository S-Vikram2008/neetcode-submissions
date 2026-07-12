class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left=0;
        int right=numbers.size()-1;
        vector <int> result={-1,-1};

        while (left<right){
            if ((numbers[left]+numbers[right])<target){
                left++ ;
            }
            else if ((numbers[left]+numbers[right])>target){
                right--;
            }
            else {
                result[0] = left+1;
                result[1] = right+1;
                return result;
            }
        }
        
    }
};
