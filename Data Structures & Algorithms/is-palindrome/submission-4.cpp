
class Solution {
public:
    bool isPalindrome(string s) {
        #include <cctype>
        string sub;

        for (int i=0;i<s.length();i++){
            if (isalnum(s[i])){
                sub+=tolower(s[i]);
            }
        }

        int left=0;
        int right=sub.length()-1;

        while (left<right){
            if (sub[left]!=sub[right]){
                return false;
            }
            left+=1;
            right-=1;
        }
       
        return true;
        
        
        
    }
};
