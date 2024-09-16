class Solution {
public:
    int countSubstrings(string s) {
        // input = aaa 
        // count itself first - count = string.length()
        // palindorme logic - order of letters is same both ways 
        // for(i - 0 to i - n)
        // for (j - n to j -0)
        // if(s[i] == s[j])
        //{
            // count++
        //}
        // count strings following this logic 
        // return count

        int n = s.length();
        int count = 0;
        int l = s[0];
        int r = s[n];

        for(int i =0; i<n; i++)
        {
            if(l==r)
            {
                count++;
                l++;
                r--;
            }
           
        }

        return count;
        
    }
};