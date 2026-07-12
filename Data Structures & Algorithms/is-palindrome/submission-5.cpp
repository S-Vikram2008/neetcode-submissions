
class Solution {
public:
    bool isPalindrome(string s) {
        #include <cctype>

        /* for (int i=0;i<s.length();i++){
            if (isalnum(s[i])){
                sub+=tolower(s[i]);
            }
        } */


        int left=0;
        int right=s.length()-1;

        while (left<right){
            if (not (isalnum(s[left]))){
                left+=1;
            }
            else if (not (isalnum(s[right]))){
                right-=1;
            }
            else if (tolower(s[left])!=tolower(s[right])){
                return false;
            }
            else{

            
            left+=1;
            right-=1;
            }
        }
       
        return true;
        
        
        
    }
};
