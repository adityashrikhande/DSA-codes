
// dp tabulation

class Solution {
    public boolean canPartition(int[] nums) {
        
        int n = nums.length;
        int sum = 0;
        for(int ele : nums){
            sum += ele;
        }
        if (sum%2 != 0){
            return false;
        }
        int half = sum/2;
        System.out.println(half);
        int dp[][] = new int[n+1][half+1];
        
        for(int i=0; i<=n; i++){
            dp[i][0] = 1;
        }
        //dp[0][nums[0]] = 1;
        for(int i=1; i<=n; i++){
            for(int j=1; j<=half; j++){
                int take = 0;
                if (nums[i-1] <= j){
                    take = dp[i-1][j-nums[i-1]];
                }
                int nottake = dp[i-1][j];
                if (take == 1 || nottake == 1){
                    dp[i][j] = 1;
                }else{
                    dp[i][j] = 0;
                }
            }
        }
        return dp[n][half] == 1 ? true : false;
        
    }
}

// rec + memo

class Solutio {
    
    public int solve(int[] nums, int i, int sum, int[][] dp){
        if (sum == 0){
            return 1;
        }
        if (dp[i][sum] != -1){
            return dp[i][sum];
        }
        if(i == 0){
            return nums[i] == sum ? 1 : 0;
        }
        
        int a = 0;
        if (nums[i] <= sum){
            a = solve(nums, i-1, sum-nums[i], dp);
        }
        int b = solve(nums, i-1, sum, dp);
        
        if (a == 1 || b == 1){
            return dp[i][sum] = 1;
        }else{
            return dp[i][sum] = 0;
        }
        
    }
    
    public boolean canPartition(int[] nums) {
        
        int sum = 0;
        for(int ele : nums){
            sum += ele;
        }
        if (sum%2 != 0){
            return false;
        }
        
        int dp[][] = new int[nums.length][sum/2+1];
        
        for(int i=0; i<nums.length; i++){
            for(int j=0; j<=sum/2; j++){
                dp[i][j] = -1;
            }
        }
        
        if (solve(nums, nums.length-1, sum/2, dp) == 1){
            return true;
        }else{
            return false;
        }
    }
}
