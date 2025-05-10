class Solution {
public:
    bool isPalindrome(string s) {
        char fr;
        char ba;
        int f=0;
        int b=s.size()-1;
        while(f<b){
            // std::cout<<s[f]<<isalnum(s[f])<<"\n";
            while(!std::isalnum(s[f]) && f<b){
                f++;
            }
            while(!std::isalnum(s[b]) &&b>f){
                b--;
            }
            if(f<b){
                fr=tolower(s[f]);
                ba=tolower(s[b]);
                if(fr!=ba){
                    return false;
                }

            }
            f++;
            b--;
            
        }
        return true;
        
    }
};
