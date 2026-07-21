class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        #include <queue>
        priority_queue <int> pq;

        int outcome;

        for (int x:nums)
            pq.push(x);
        
        for (int i=0;i<k;i++)
        {
            outcome=pq.top();
            pq.pop();

        }

        return outcome;
        




    }
};
