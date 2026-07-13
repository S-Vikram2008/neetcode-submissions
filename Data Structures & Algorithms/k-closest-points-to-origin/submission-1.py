class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # NOTE : HERE WE DONT TAKE SQUARE ROOT WHILE PERFORMING DISTANCE CALCULATION AS 
        # TAKING SQUARE ROOT INCREASES SOME TIME COMPLEXITY .
        
        # Importing necessary modules 
        import heapq
        
        d=[] # Empty list to store (distance,coordinates) values
        heapq.heapify(d) # Converting list 'd' to a  min heap
        answer=[] # Final answer list which will be returned 

        for i in points :
            distance=i[0]**2+i[1]**2
            heapq.heappush(d,(distance,[i[0],i[1]]))

        for i in range(k):
            outcome=heapq.heappop(d)
            answer.append(outcome[1])

        return answer
