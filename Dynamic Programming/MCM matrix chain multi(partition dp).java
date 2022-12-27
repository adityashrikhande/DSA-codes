
// Recursion + memorisation

class Solution{
    
    static long mcm(int[] arr, int i, int j, int[][] dp)
    {
        // code here
        if(i == j){
            return 0;
        }
        
        if (dp[i][j] != -1){
            return dp[i][j];
        }
        
        long mini = Integer.MAX_VALUE;
        
        for(int k=i; k<j; k++){
            long steps = arr[i-1] * arr[k] * arr[j] + mcm(arr, i, k, dp) + mcm(arr, k+1, j, dp);
            mini = Math.min(mini, steps);
        }
        return dp[i][j] = (int)mini;
    }
    
    static int matrixMultiplication(int N, int arr[])
    {
        // code here
        int dp[][] = new int[N][N];
        
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                dp[i][j] = -1;
            }
        }
        
        return (int)mcm(arr, 1, N-1, dp);
    }
}

// DP tabulation

class Solutio{
    
    static long mcm(int[] arr, int[][] dp)
    {
        // code here
        for(int i=arr.length-1; i>=1; i--){
            for(int j=i+1; j<arr.length; j++){
                dp[i][j] = Integer.MAX_VALUE;
                for(int k=i; k<j; k++){
                    dp[i][j] = Math.min(dp[i][j], dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j]);
                }
            }
        }
        return dp[1][arr.length-1];
    }
    
    static int matrixMultiplication(int N, int arr[])
    {
        // code here
        int dp[][] = new int[N][N];
        
        return (int)mcm(arr, dp);
    }
}