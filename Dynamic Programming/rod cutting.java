
// recursion + memo

import java.util.*;

class Solution {
    
    public static int solve(int price[], int ind, int n,int[][] dp){
        
        if (ind == 0){
            return price[0]*n;
        }
        if (dp[ind][n] != -1){
            return dp[ind][n];
        }
        
        int take = Integer.MIN_VALUE;
        int nottake = solve(price, ind-1, n, dp);
        if (ind+1 <= n){
            take = price[ind] + solve(price, ind, n-(ind+1), dp);
        }
        return dp[ind][n] = Math.max(take, nottake);
    }
    
    public static int cutRod(int price[], int n) {
        // Write your code here.
        int[][] dp = new int[n][n+1];
        
        for(int i=0; i<n; i++){
            Arrays.fill(dp[i], -1);
        }
        
        return solve(price, n-1, n, dp);
    }
}

// dp tabulation

class Solutio {
    
    public static int cutRod(int price[], int n) {
        // Write your code here.
        int[][] dp = new int[n][n+1];
        
        for(int i=0; i<=n; i++){
            dp[0][i] = price[0]*i;
        }
        
        for(int ind=1; ind<n; ind++){
            for(int j=0; j<=n; j++){
                int take = Integer.MIN_VALUE;
                int nottake = dp[ind-1][j];
                if (ind+1 <= j){
                    take = price[ind] + dp[ind][j-(ind+1)];
                }
                dp[ind][j] = Math.max(take, nottake);
            }
        }
        return dp[n-1][n];
    }
}