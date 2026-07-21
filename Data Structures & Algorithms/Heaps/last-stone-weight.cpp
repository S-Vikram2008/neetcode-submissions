class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        #include <queue>
        using namespace std;

        int first=0,second=0;
        priority_queue<int> pq;

        for(int x : stones)
            pq.push(x);

        while (pq.size()>1){
            first=pq.top();
            pq.pop();
            second=pq.top();
            pq.pop();

            if (first!=second){
                pq.push(abs(first-second));
        }
        
    }
        if (pq.empty())
            return 0;
        else
            return pq.top();
    }
};
