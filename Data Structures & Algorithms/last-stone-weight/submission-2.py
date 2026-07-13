class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-x for x in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            x=heapq.heappop(stones)
            y=heapq.heappop(stones)

            if (x>y):
                heapq.heappush(stones,y-x)
            
            elif (y>x):
                heapq.heappush(stones,x-y)
            
        else:
            if stones!=[]:
                stones=[-x for x in stones]
                return stones[0]
            else:
                return 0
            
        

        

