class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_map=dict()
        t_map=dict()

        if len(s)!=len(t):
            return False
        else:

            for i in s:
                if i not in s_map:
                    s_map[i]=1
                else:
                    s_map[i]+=1
            
            for i in t:
                if i not in t_map:
                    t_map[i]=1
                else:
                    t_map[i]+=1
            
            if s_map==t_map:
                return True
            else:
                return False
