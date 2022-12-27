
// rec + memo

import java.util.*;
class Solution {
    
    public int solve(int[] cuts, int i, int j, int first, int last, int[][] dp){
        if (i > j){
            return 0;
        }
        
        if (dp[i][j] != -1){
            return dp[i][j];
        }
        
        long mini = Integer.MAX_VALUE;
        
        for(int k=i; k<=j; k++){
            
            long ans = last-first + solve(cuts, i, k-1, first, cuts[k], dp) + solve(cuts, k+1, j, cuts[k], last, dp);
            mini = Math.min(mini, ans);
        }
        return dp[i][j] = (int)mini;
    }
    
    public int minCost(int n, int[] cuts) {
        
        Arrays.sort(cuts);
        int l = cuts.length;
        
        int[][] dp = new int[l][n];
        
        for(int i=0; i<l; i++){
            for(int j=0; j<n; j++){
                dp[i][j] = -1;
            }
        }
        
        return solve(cuts, 0, cuts.length-1, 0, n, dp);
    }
}

// dp tabulation

//import java.util.*;
class Solutio {
    
    public int minCost(int x, int[] cuts) {
        
        Arrays.sort(cuts);
        int n = cuts.length;
        int arr[] = new int[n+2];
        for(int i=1; i<=n; i++){
            arr[i] = cuts[i-1];
        }
        arr[n+1] = x;
        arr[0] = 0;
        int m = arr.length;
        
        int[][] dp = new int[m][m];
        
        for(int i=m-1; i>=1; i--){
            for(int j=i; j<=m-2; j++){

                long mini = Integer.MAX_VALUE;

                for(int k=i; k<=j; k++){

                    long ans = arr[j+1]-arr[i-1] + dp[i][k-1] + dp[k+1][j];
                    mini = Math.min(mini, ans);
                }
                dp[i][j] = (int)mini;
            }
        }
        
        return dp[1][m-2];
    }
}
