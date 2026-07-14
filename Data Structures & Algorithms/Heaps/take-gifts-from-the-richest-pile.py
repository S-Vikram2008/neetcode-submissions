class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        import math
        gifts=[-x for x in gifts]

        import heapq
        heapq.heapify(gifts)

        for i in range(k):
            outcome=-heapq.heappop(gifts)
            heapq.heappush(gifts,-1*(math.floor(outcome**0.5)))
        
        gifts=[-x for x in gifts]

        sum=0
        for i in range(len(gifts)):
            sum+=heapq.heappop(gifts)
        
        return sum
