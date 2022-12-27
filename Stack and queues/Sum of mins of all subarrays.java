import java.util.*;
//import java.lang.*;
//import java.io.*;

class Pair{
        int first, second;
        Pair(int f, int s){
                this.first = f;
                this.second = s;
        }
}

class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		//your code here
                Scanner sc = new Scanner(System.in);
                int n = sc.nextInt();
                int arr[] = new int[n];
                int left[] = new int[n];
                int right[] = new int[n];
                
                for(int i=0; i<n; i++){
                        arr[i] = sc.nextInt();
                        left[i] = 1;
                        right[i] = 1;
                }
                
                Stack<Pair> st = new Stack<Pair>();
                st.push(new Pair(arr[0], 1));

                for(int i=1; i<n; i++){
                        while(!st.isEmpty() && st.peek().first >= arr[i]){
                                left[i] += st.pop().second;
                        }
                        st.push(new Pair(arr[i], left[i]));
                }
                
                st = new Stack<Pair>();
                st.push(new Pair(arr[n-1], 1));
                        
                for(int i=n-2; i>=0; i--){
                        while(!st.isEmpty() && st.peek().first > arr[i]){
                                right[i] += st.pop().second;
                        }
                        st.push(new Pair(arr[i], right[i]));
                }
                long sum = 0;
                long mod = 1000000007;

                for(int i=0; i<n; i++){
                        sum += (left[i]*right[i]*arr[i]);
                }
                sc.close();
                System.out.println(sum%mod);
	}
}
