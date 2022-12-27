

//import java.io.*;
import java.util.*;


class Main {
	public static void main (String[] args)
	{
		Scanner sc = new Scanner(System.in);
	    
	    	int n = sc.nextInt();
			int[] A = new int[n];
	    	for(int i=0;i<n;i++)
	        A[i] = sc.nextInt();
            
	    	Solution Obj= new Solution();
	    	
            System.out.println(Obj.nTriang(A));
            sc.close();

	}
  
}
class Solution{
	public int nTriang(int[] arr) {
      // your code goes here
		long mod = 1000000007l;
		int n = arr.length;
		
		Arrays.sort(arr);
		long ans = 0;
		for(int i=0; i<n-2; i++)
		{ 
			int l = i+1, r = i+2;
			while(l<n && r < n){ 
				if(arr[r] < arr[l] + arr[i]){
					ans += (r - l);
					r++;
					ans %= mod;
				}else{
					l++;
					if(l>=r){
						r++;
					} 
				} 
			}
		} return (int)ans; 
	}
}

