class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        n=[-x for x in nums]
        heapq.heapify(n)

        for i in range(k-1):
            heapq.heappop(n)
        
        
        return -heapq.heappop(n)
