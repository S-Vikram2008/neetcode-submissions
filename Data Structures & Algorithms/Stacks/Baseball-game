class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        sum=0
        for i in operations:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
                sum+=int(i)
            elif i in ('+','C','D'):
                if  stack!=[] and i=='+':
                    sum+=int(stack[-1])+int(stack[-2])
                    stack.append(int(stack[-1])+int(stack[-2]))
                    
                elif  stack!=[] and  i=='C':
                    deleted=stack.pop()
                    sum-=deleted
                
                elif  stack!=[] and i=='D':
                    sum+=int(stack[-1]*2)
                    stack.append(int(stack[-1]*2))
                
        
        return sum
