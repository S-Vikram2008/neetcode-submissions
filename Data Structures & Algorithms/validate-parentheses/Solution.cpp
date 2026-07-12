class Solution {
public:
    bool isValid(string s) {
        vector <char> stack;

        for (int i=0;i<s.length();i++){
            if ((s[i]=='{')|| (s[i]=='[')||(s[i]=='(')){
                stack.push_back(s[i]);
            }
            else{
                if (s[i]==')'){
                    if (not stack.empty() and stack.back()=='('){
                        stack.pop_back();
                    }
                    else{
                        return false;
                    }
                }
                

                if (s[i]=='}'){
                    if (not stack.empty() and stack.back()=='{'){
                        stack.pop_back();
                    
                    }
                     else{
                        return false;
                    }
                }
               

                if (s[i]==']'){
                    if (not stack.empty() and stack.back()=='['){
                        stack.pop_back();
                    }
                    else{
                        return false;
                }
                }
                

                




            }
            
        }
        return stack.size()==0;
    }
};
