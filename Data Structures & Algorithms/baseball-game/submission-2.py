class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in operations:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            elif i in ('+','C','D'):
                if  stack!=[] and i=='+':
                    stack.append(int(stack[-1])+int(stack[-2]))
                elif  stack!=[] and  i=='C':
                    stack.pop()
                
                elif  stack!=[] and i=='D':
                    stack.append(int(stack[-1]*2))
                
        
        return sum(stack)