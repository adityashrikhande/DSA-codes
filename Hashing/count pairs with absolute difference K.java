
//import java.io.*;
import java.util.*;

class Solution {
    public long pairDifference(int []A, int n, int k) {
       // write code here
		long count = 0;
		HashMap<Integer, Integer> mp = new HashMap<>();
		for(int i=0; i<n; i++){
			if(!mp.containsKey(A[i])){
				mp.put(A[i], 1);
			}else{
				mp.put(A[i], mp.get(A[i]) + 1);
			}
		}
		for(int i=0; i<n; i++){
			if(k == 0){
				if(mp.containsKey(A[i]) && mp.get(A[i]) > 1){
					count++;
					mp.remove(A[i]);
				}
			}else{
				if(mp.containsKey(k+A[i])){
					count++;
				}
				if(mp.containsKey(A[i]-k)){
					count++;
				}
				mp.remove(A[i]);
			}
		}
		return count;
    }
}
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n,k;
        n = sc.nextInt();
        k = sc.nextInt();
        int []mat=new int[n];
        for(int i=0;i<n;++i){
            mat[i]=sc.nextInt();
        }
        Solution Obj = new Solution();
        System.out.println(Obj.pairDifference(mat,n,k));
        System.out.println('\n');
        sc.close();
    }
}