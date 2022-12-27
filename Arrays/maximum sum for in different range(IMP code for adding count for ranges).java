
import java.util.*;
//import java.lang.*;
import java.io.*;

class Main {
    
    public static int maximumSum(int[] A, int[][] ops) {
	    int cnt[] = new int[A.length];
	    for (int[] r : ops) {
	        cnt[r[0]] += 1;
	        if (r[1] + 1 < A.length)
	            cnt[r[1] + 1] -= 1;
	    }
	    for (int i = 1; i < cnt.length; ++i)
	        cnt[i] += cnt[i - 1];
	    Arrays.sort(A);
	    Arrays.sort(cnt);
	    long res = 0;
	    for (int i = 0; i < A.length; ++i)
	        res = (res + (long)A[i] * cnt[i]) % 1000000007;
	    return (int)res;
    }
	public static void main (String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));	
        long n = Long.parseLong(br.readLine().trim());
        String inputLine[] = br.readLine().trim().split(" ");
        int[] arr = new int[(int)n];
        for(int i=0; i<n; i++)arr[i]=Integer.parseInt(inputLine[i]);
        long m = Long.parseLong(br.readLine().trim());
        int[][] ops = new int[(int)m][2];
        for(int i=0; i<m; i++){
          String inputLine1[] = br.readLine().trim().split(" ");
          ops[i][0]=Integer.parseInt(inputLine1[0]);
          ops[i][1]=Integer.parseInt(inputLine1[1]);
        }
        System.out.println(maximumSum(arr, ops));
	}
}
