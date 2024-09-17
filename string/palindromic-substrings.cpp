//brute force
class Solution {
public:

int countPalindrome(string s, int l, int r)
{
    int count = 0;
    int n = s.length();
     while(l>=0 && r<n && s[l] == s[r])
            {
                count++;
                l--;
                r++;
            }
            return count;
}

    int countSubstrings(string s) {
        // odd palindromes
       // l == r, then start exapnding, if they're still equal increase count, other wise move to next element  
        // even palindrome 
        // l = s[0], r = l+1, if l==r, count++, and move to next ones, if not, still move to next ones 
        // do both even and odd palindromes and return total count

        int count =0;
        int n = s.length();

        for(int i =0; i<n; i++)
        {
            //odd palindrome
            // int l = i;
            // int r = i;
            count += countPalindrome(s, i, i);
            
            //even palindrome
            // l = i;
            // r = i+1;
            count += countPalindrome(s, i, i+1);
             


        }

        return count;

    }
       
};

// //brute force
// class Solution {
// public:

// bool isPalindrome(string s, int start, int end)
// {
//     int n = s.length();
//     for(int i=0; i<n; i++)
//     {
//         if(s[start] != s[end])
//         {
//             return false;
//         }
//     }
//     return true;
// }
//     int countSubstrings(string s) {
//         // check for each character if it's subtring is plaindromic
//         //brute force - 
//         int count= 0;
//         int n =s.length();

//         for(int i=0; i<n; i++)
//         {
//             for(int j =i; j<n; j++)
//             {
//                 if(isPalindrome(s,i,j))
//                 {
//                     count++;
//                 }
//             }
//         } 
//         return count;
//         }
       
// };