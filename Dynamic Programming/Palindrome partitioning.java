import java.util.*;
class Solution{
    
    static boolean checkPalindrome(int a, int b, String str){
        int left = a;
        int right = b;
        
        while(left < right){
            if(str.charAt(left) != str.charAt(right))return false;
            left++;
            right--;
        }
        return true;
    }
    
    static int solve(int idx, String str, int dp[]){
        if(idx == str.length())return 0;
        
        if(dp[idx] != -1)return dp[idx];
        
        int minpartition = Integer.MAX_VALUE;
        
        for(int i=idx; i<str.length(); i++){
            if(checkPalindrome(idx, i, str)){
                int temp = 1 + solve(i+1, str, dp);
                minpartition = Math.min(minpartition, temp);
            }
        }
        return dp[idx] = minpartition;
    }
    
    static int palindromicPartition(String str)
    {
        // code here
        int dp[] = new int[str.length()];
        Arrays.fill(dp, -1);
        
        return solve(0, str, dp)-1;
    }
}
