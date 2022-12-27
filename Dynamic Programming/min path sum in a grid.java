
// recursion + memo

class Solution {
    
    public int solve(int[][] grid, int i, int j, int[][] dp){
        
        if (i == grid.length-1 && j == grid[0].length-1){
            return grid[i][j];
        }
        
        if (dp[i][j] != -1){
            return dp[i][j];
        }
        
        if (i + 1 == grid.length){
            return dp[i][j] = grid[i][j] + solve(grid, i, j+1, dp);
        }
        if (j + 1 == grid[0].length){
            return dp[i][j] = grid[i][j] + solve(grid, i+1, j, dp);
        }
        return dp[i][j] = grid[i][j] + Math.min(solve(grid, i+1, j, dp), solve(grid, i, j+1, dp));
    }
    
    public int minPathSum(int[][] grid) {
        
        int n = grid.length;
        int m = grid[0].length;
        
        int dp[][] = new int[n][m];
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                dp[i][j] = -1;
            }
        }
        return solve(grid, 0, 0, dp);
    }
}

// dp tabulation

class Solutio {
    
    
    public int minPathSum(int[][] grid) {
        
        int n = grid.length;
        int m = grid[0].length;
        
        int dp[][] = new int[n+1][m+1];
        for(int i=1; i<=n; i++){
            for(int j=1; j<=m; j++){
                if (i == 1){
                    dp[i][j] = grid[i-1][j-1] + dp[i][j-1];
                }else if(j == 1){
                    dp[i][j] = grid[i-1][j-1] + dp[i-1][j];
                }else{
                    dp[i][j] = grid[i-1][j-1] + Math.min(dp[i-1][j], dp[i][j-1]);
                }   
            }
        }
        return dp[n][m];
    }
}
