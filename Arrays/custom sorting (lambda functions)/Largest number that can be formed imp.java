
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
                ArrayList<String> arr = new ArrayList<String>();
        
                for(int i=0; i<n; i++){ 
                        int x = sc.nextInt();
                    arr.add(String.valueOf(x));
                }
                if(n == 1){
                    System.out.print(arr.get(0));
                }
                //System.out.println("acd".compareTo("def"));
                Collections.sort(arr, (x, y) -> (y+x).compareTo(x+y));
        
                for(int i=0; i<n; i++){
                        System.out.print(arr.get(i));
                }
                sc.close();
	}
}