class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        #include <cmath>
        #include <queue>
        priority_queue<int> pq;
        int sum=0;
        int first;

        for (int x:gifts)
            pq.push(x);

        for(int i=0;i<k;i++){
            
            first=pq.top();
            pq.pop();

            pq.push(floor(pow(first,0.5)));

        }
        while (not pq.empty()){
            sum+=pq.top();
            pq.pop();
        }
        return sum;
    }
    
};