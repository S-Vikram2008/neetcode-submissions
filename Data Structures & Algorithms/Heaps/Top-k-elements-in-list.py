class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       import heapq
       
       heap=[]
       heapq.heapify(heap)

       hashmap=dict()

       for i in nums:
        if i not in hashmap:
            hashmap[i]=1
        else:
            hashmap[i]+=1
       
       for i in hashmap:
        heapq.heappush(heap,(-hashmap[i],i))
       
       answer=[]
       for i in range(k):
        answer.append(heapq.heappop(heap)[1])

       
       return answer
       

        

        
