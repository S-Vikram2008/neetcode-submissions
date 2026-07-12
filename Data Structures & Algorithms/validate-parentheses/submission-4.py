class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in ('(', '{', '['):
                stack.append(i)
            else:
                if i == ')':
                    if not stack or stack[-1] != '(':
                        return False
                    else:
                        stack.pop()

                elif i == '}':
                    if not stack or stack[-1] != '{':
                        return False
                    else:
                        stack.pop()

                elif i == ']':
                    if not stack or stack[-1] != '[':
                        return False
                    else:
                        stack.pop()

        return len(stack) == 0