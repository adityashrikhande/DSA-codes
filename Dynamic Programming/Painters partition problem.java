
// recursion

import java.util.*;
import java.io.*;
 
class GFG
{
// function to calculate sum between two indices
// in array
static int sum(int arr[], int from, int to)
{
    int total = 0;
    for (int i = from; i <= to; i++)
        total += arr[i];
    return total;
}
  
// for n boards and k partitions
static int partition(int arr[], int n, int k)
{
    // base cases   
    if (k == 1) // one partition
        return sum(arr, 0, n - 1);   
    if (n == 1)  // one board
        return arr[0];
  
    int best = Integer.MAX_VALUE;
  
    // find minimum of all possible maximum
    // k-1 partitions to the left of arr[i],
    // with i elements, put k-1 th divider
    // between arr[i-1] & arr[i] to get k-th
    // partition
    for (int i = 1; i <= n; i++)
        best = Math.min(best, Math.max(partition(arr, i, k - 1),
                                sum(arr, i, n - 1)));
  
    return best;
}
 
// Driver code
public static void main(String args[])
{
 int arr[] = { 10, 20, 60, 50, 30, 40 };
  
    // Calculate size of array.
    int n = arr.length;
        int k = 3;
 System.out.println(partition(arr, n, k));
}
}


// dp tabulation

class GFG1
{
// function to calculate sum between two indices
// in array
static int sum(int arr[], int from, int to)
{
    int total = 0;
    for (int i = from; i <= to; i++)
        total += arr[i];
    return total;
}
  
// bottom up tabular dp
static int findMax(int arr[], int n, int k)
{
    // initialize table
    int dp[][] = new int[k+1][n+1];
  
    // base cases
    // k=1
    for (int i = 1; i <= n; i++)
        dp[1][i] = sum(arr, 0, i - 1);
  
    // n=1
    for (int i = 1; i <= k; i++)
        dp[i][1] = arr[0];
  
    // 2 to k partitions
    for (int i = 2; i <= k; i++) { // 2 to n boards
        for (int j = 2; j <= n; j++) {
  
            // track minimum
            int best = Integer.MAX_VALUE;
  
            // i-1 th separator before position arr[p=1..j]
            for (int p = 1; p <= j; p++)
                best = Math.min(best, Math.max(dp[i - 1][p],
                              sum(arr, p, j - 1)));      
  
            dp[i][j] = best;
        }
    }
  
    // required
    return dp[k][n];
}
 
