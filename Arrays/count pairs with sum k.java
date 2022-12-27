import java.util.*;
//import java.lang.*;
//import java.io.*;


class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		//your code here
                Scanner sc = new Scanner(System.in);
                int n = sc.nextInt();
                int arr[] = new int[n];
                for(int i=0; i<n; i++){
                        arr[i] = sc.nextInt();
                }
                int k = sc.nextInt();
                HashMap<Integer, Integer> mp = new HashMap<>();
                int cnt = 0;
                for(int i=0; i<n; i++){
                        if(!mp.containsKey(arr[i])){
                                mp.put(arr[i], 0);
                        }
                        mp.put(arr[i], 1 + mp.get(arr[i]));
                }
                for(int i=0; i<n; i++){
                        if(mp.containsKey(k-arr[i])){
                                cnt += mp.get(k-arr[i]);
                        }
                        if(arr[i] == k-arr[i]){
                                cnt--;
                        }
                }
                System.out.println(cnt/2);
                sc.close();
	}
}
