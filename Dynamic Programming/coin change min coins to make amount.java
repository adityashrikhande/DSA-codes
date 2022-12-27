
// rec + memo

class Solution {
    
    public int solve(int[] coins, int amount, int i, int[][] dp){
        
        if(i == coins.length){
            return 100000000;
        }
        if (amount == 0){
            return dp[i][amount] = 0;
        }
        
        if(dp[i][amount] != -1){
            return dp[i][amount];
        }
        
        if (coins[i] > amount){
            return dp[i][amount] = solve(coins, amount, i+1, dp);
        }else{
            return dp[i][amount] = Math.min(solve(coins, amount, i+1, dp), 1 + solve(coins, amount-coins[i], i, dp));
        }
        
    }
    
    public int coinChange(int[] coins, int amount) {
        
        if (amount == 0){
            return 0;
        }
        
        int n = coins.length;
        int dp[][] = new int[n+1][amount+1];
        
         for(int i=0; i<=n; i++){
            for(int j=0; j<=amount; j++){
                dp[i][j] = -1;
            }
        }
        
        int ans = solve(coins, amount, 0, dp);
        if (ans >= 100000000){
            return -1;
        }else{
            return ans;
        }
    }
}

// dp tabulation

class Solutio {
    
    public int solve(int[] coins, int amount, int i, int[][] dp){
        
        if(i == coins.length){
            return 100000000;
        }
        if (amount == 0){
            return dp[i][amount] = 0;
        }
        
        if(dp[i][amount] != -1){
            return dp[i][amount];
        }
        
        if (coins[i] > amount){
            return dp[i][amount] = solve(coins, amount, i+1, dp);
        }else{
            return dp[i][amount] = Math.min(solve(coins, amount, i+1, dp), 1 + solve(coins, amount-coins[i], i, dp));
        }
        
    }
    
    public int coinChange(int[] coins, int amount) {
        
        if (amount == 0){
            return 0;
        }
        
        int n = coins.length;
        int dp[][] = new int[n+1][amount+1];
        
        for(int i=0; i<=amount; i++){
            dp[0][i] = 100000000;
        }
        
        for(int i=1; i<=n; i++){
            for(int j=1; j<=amount; j++){
                if (coins[i-1] > j){
                    dp[i][j] = dp[i-1][j];
                }else{
                    dp[i][j] = Math.min(dp[i-1][j], 1 + dp[i][j-coins[i-1]]);
                }
            }
        }
        if (dp[n][amount] >= 100000000){
            return -1;
        }
        return dp[n][amount];
    }
}    


// dp space optimisation

class Soluti {
    
    public int coinChange(int[] coins, int amount) {
        
        if (amount == 0){
            return 0;
        }
        
        int n = coins.length;
        int cur[] = new int[amount+1];
        int[] prev = new int[amount+1];
        
        for(int i=0; i<=amount; i++){
            prev[i] = 100000000;
        }
        
        for(int i=1; i<=n; i++){
            for(int j=1; j<=amount; j++){
                if (coins[i-1] > j){
                    cur[j] = prev[j];
                }else{
                    cur[j] = Math.min(prev[j], 1 + cur[j-coins[i-1]]);
                }
            }
            prev = cur;
        }
        if (prev[amount] >= 100000000){
            return -1;
        }
        return prev[amount];
        
    }
}

