
import java.util.*;
//import java.lang.*;
//import java.io.*;
// https://course.acciojob.com/idle?question=9fa66613-25ce-4390-99a0-d3ae2f3825ba
class Main
{

        public static boolean isPossibleMarker(int[] arr, int n, int marker, int minFruitCount){

                boolean flag = false;
                int fruitSum = 0;
                for(int i=0; i<n; i++){
                        if(arr[i] > marker){
                                fruitSum += arr[i]-marker;
                        }
                        if(fruitSum >= minFruitCount){
                                flag = true;
                                break;
                        }
                }
                return flag;
        }

        public static int binarySearch(int[] arr, int n, int maxi, int minFruitCount){
                int low = 0;
                int high = maxi;

                while(low <= high){
                        int mid = (low+high)/2;
                        if(isPossibleMarker(arr, n, mid, minFruitCount)){
                                low = mid+1;
                        }else{
                                high = mid-1;
                        }
                }
                return high;
        }
        
	public static void main (String[] args) throws java.lang.Exception
	{
		//your code here
                Scanner sc = new Scanner(System.in);
                int n = sc.nextInt();
                int m = sc.nextInt();
                int arr[] = new int[n];

                int maximumelement = -1;
                for(int i=0; i<n; i++){
                        arr[i] = sc.nextInt();
                        maximumelement = Math.max(maximumelement, arr[i]);
                }
                sc.close();
                int ans = binarySearch(arr, n, maximumelement, m);
                System.out.println(ans);
	}
}