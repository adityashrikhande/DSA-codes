
import java.io.*;
import java.util.*;


class Solution{
    public String smallestNumber(String str){
        // write code here
		int n = str.length() + 1;
		int arr[] = new int[n];
		int count = 1;

		for(int i=0; i<n-1; i++){
			if(str.charAt(i) == 'i'){
				int idx = i;
				while(idx >= 0 && arr[idx] == 0){
					arr[idx] = count++;
					idx--;
				}
			}
		}
		int idx = n-1;
		while(idx >= 0 && arr[idx] == 0){
			arr[idx] = count++;
			idx--;
		}
		String ans = "";
		for(int i=0; i<n; i++){
			ans += arr[i]+"";
		}
		return ans;
    }
}

public class Main {

  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String str = br.readLine();
    Solution Obj = new Solution();
    System.out.print(Obj.smallestNumber(str));
  }
}