import java.util.*;
class Sol
{
    
    public static boolean find(String s, ArrayList<String> arr){
        for(int i=0; i<arr.size(); i++){
            if(s.compareTo(arr.get(i)) == 0){
                return true;
            }
        }
        return false;
    }
    
    public static boolean solve(String s, ArrayList<String> arr, int idx, String ans){
        
        if(idx == s.length())return true;
        
        for(int i=idx; i<s.length(); i++){
            ans += s.charAt(i);
            if(find(ans, arr)){
                if(solve(s, arr, i+1, "") == true){
                    return true;
                }
            }
        }
        return false;
    }
    
    public static int wordBreak(String A, ArrayList<String> B )
    {
        //code here
        if(solve(A, B, 0, "")){
            return 1;
        }
        return 0;
    }
}

// Rec + MEMO

class Sol1
{
    public static int find(String s, ArrayList<String> arr){
        for(int i=0; i<arr.size(); i++){
            if(s.compareTo(arr.get(i)) == 0){
                return 1;
            }
        }
        return 0;
    }
    
    public static int solve(String s, ArrayList<String> arr, int idx, String ans, int[] dp){
        
        if(idx == s.length())return 1;
        
        if(dp[idx] != -1){
            return dp[idx];
        }
        for(int i=idx; i<s.length(); i++){
            ans += s.charAt(i);
            if(find(ans, arr) == 1){
                if(solve(s, arr, i+1, "", dp) == 1){
                    return dp[i] = 1;
                }
            }
        }
        return dp[idx] = 0;
    }
    
    public static int wordBreak(String A, ArrayList<String> B )
    {
        //code here
        int dp[] = new int[A.length()];
        
        Arrays.fill(dp, -1);
        
        return solve(A, B, 0, "", dp);
    }
}

// DP solution

class Sol2
{
    public static int find(String s, ArrayList<String> arr){
        for(int i=0; i<arr.size(); i++){
            if(s.compareTo(arr.get(i)) == 0){
                return 1;
            }
        }
        return 0;
    }

public static int wordBreak(String A, ArrayList<String> B )
    {
        //code here
        int n = A.length()+1;
        int dp[] = new int[n];
        dp[0] = 1;
        
        for(int i=1; i<n; i++){
            for(int j=0; j<n-1; j++){
                if(dp[j] == 1 && find(A.substring(j, i), B) == 1){
                    dp[i] = 1;
                    break;
                }
            }
        }
        return dp[n-1];
    }
}
