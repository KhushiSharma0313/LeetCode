class Solution {
public:

bool isPalindrome(string s, int start, int end)
{
    while(start <end)
    {
        if(s[start] != s[end])
        {
            return false;
        }
        start++;
        end--;

    }
    return true;
}
    int countSubstrings(string s) {
        // go through each element 
        // then for each element go through it's substring 
        // then check if substring is plaindrome or not 

        int n = s.length();
        int count = 0;

        for(int i =0; i <n; i++)
        {
            for(int j =i; j < n; j++)
            {
                if(isPalindrome(s, i, j))
                {
                    count++;
                }
            }
        }
         return count;
        }
       
};