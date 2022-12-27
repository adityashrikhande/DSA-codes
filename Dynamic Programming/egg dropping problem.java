class Solution 
{
    
    static int solve(int e, int k, int dp[][]){
        if(k == 0 || k == 1 || e == 1)return k;
        
        if(dp[e][k] != -1)return dp[e][k];
        
        int mini = Integer.MAX_VALUE;
        
        for(int f=1; f<=k; f++){
            int temp = 1 + Math.max(solve(e-1, f-1, dp), solve(e, k-f, dp));
            
            mini = Math.min(mini, temp);
        }
        return dp[e][k] = mini;
        
    }
    
    //Function to find minimum number of attempts needed in 
    //order to find the critical floor.
    static int eggDrop(int n, int k) 
	{
	    // Your code here
	    int dp[][] = new int[n+1][k+1];
	    for(int i=0; i<=n; i++){
	        for(int j=0; j<=k; j++){
	            dp[i][j] = -1;
	        }
	    }
	    return solve(n, k, dp);
	    
	}
}
