import java.util.*;
//import java.lang.*;
//import java.io.*;

class Main
{
    public static int fact(int n){
        if(n == 1)return 1;

        return n*fact(n-1);
    }

    public static void Solve(Vector<Integer> arr, int[] perm, int n, long k, int idx, long fact){

        if(n == 1){
            perm[idx] = arr.get(0);
            return;
        }
        
        long rem = (long)(k)%fact;
        long id = (long)(k)/fact;
        perm[idx]= arr.get((int)id);

        arr.remove((int)id);

        Solve(arr, perm, n-1, rem, idx+1, fact/(n-1));
    }
    
	public static void main (String[] args) throws java.lang.Exception
	{
		//your code here
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        int[] perm = new int[n];
        Vector<Integer> arr = new Vector<Integer>();
        long fact = 1;
        for(int i=1; i<=n; i++){
            fact = fact*i;
            arr.add(i);
        }
        Solve(arr, perm, n, k, 0, fact/n);

        for(int i=0; i<n; i++){
            System.out.print(perm[i] + " ");
        }
        sc.close();
	}
}