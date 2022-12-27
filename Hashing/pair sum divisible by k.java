//import java.io.*;
import java.util.*;

class Solution {
    public boolean arrayPairs(int[] arr, int k) {
		// write code here
		int rem[] = new int[k];
		int n = arr.length;
		for(int i=0; i<n; i++){
			rem[arr[i]%k]++;
		}
		
		int left = 1;
		int right = k-1;
		while(left < right){
			if(rem[left] != rem[right]){
				return false;
			}
			left++;
			right--;
		}
		return rem[0]%2 == 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n,k;
        n = sc.nextInt();
		k = sc.nextInt();
        int arr[] = new int[n];
        for(int i=0;i<n;i++)
            arr[i] = sc.nextInt();
        Solution Obj = new Solution();
        if(Obj.arrayPairs(arr,k)){
			System.out.println("true");
		}else{
			System.out.println("false");
		}
        sc.close();
    }
} 
 

