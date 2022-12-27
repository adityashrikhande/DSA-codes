
import java.util.*;
import java.lang.*;
import java.io.*;

public class Main
{
        public static void sortBySetBits(int[] arr, int n){
                ArrayList<Integer> [] count = new ArrayList [32];
                for (int i = 0; i < count.length; i++)
                        count[i] = new ArrayList<Integer>();
                for(int i=0; i<n; i++){
                        int cntbits = Integer.bitCount(arr[i]);
                        count[cntbits].add(arr[i]);
                }
                int k = 0;
                for(int i=31; i>=0; i--){
                        for(int ele: count[i]){
                                arr[k++] = ele;
                        }
                }
        }
        
	public static void main (String[] args) throws java.lang.Exception
	{
		//your code here
                Scanner sc = new Scanner(System.in);
                int t = sc.nextInt();
                for(int k=0; k<t; k++){
                        int n = sc.nextInt();
                        int[] arr = new int[n];
                        for(int i=0; i<n; i++){
                                arr[i] = sc.nextInt();
                        }
                        sortBySetBits(arr, n);
                        
                        for(int i=0; i<n; i++){
                                System.out.print(arr[i] + " ");
                        }
                        System.out.println("");
                }
	}
}