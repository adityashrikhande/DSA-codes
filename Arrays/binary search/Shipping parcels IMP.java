
import java.util.*;
//import java.lang.*;
//import java.io.*;

class Main
{

        public static boolean canBeSolved(int[] parcels, int maxWeight, int size, int days){

                int sumOfWeight = 0;
                int idx = 0;
                while(idx < size){
                        if(sumOfWeight + parcels[idx] > maxWeight){
                                days--;
                                if(days == 0){
                                        return false;
                                }
                                sumOfWeight = parcels[idx];
                        }else{
                                sumOfWeight += parcels[idx];
                        }
                        idx++;
                }
                return true;
        }

        public static int solve(int[] parcels, int size, int days, int maximumElement, int sum){

                int left = maximumElement;
                int right = sum;
                while(left < right){
                        int mid = (left+right)/2;
                        if(canBeSolved(parcels, mid, size, days)){
                                right = mid;
                        }else{
                                left = mid+1;
                        }
                }
                return right;
        }
        
	public static void main (String[] args) throws java.lang.Exception
	{
		//your code here
                Scanner sc = new Scanner(System.in);
                int size = sc.nextInt();
                int days = sc.nextInt();
                int maximumElement = -1;
                int sum = 0;
                int parcels[] = new int[size];
                for(int i=0; i<size; i++){
                        parcels[i] = sc.nextInt();
                        sum += parcels[i];
                        maximumElement = Math.max(maximumElement, parcels[i]);
                }
                sc.close();
                int ans = solve(parcels, size, days, maximumElement, sum);

                System.out.println(ans);
	}
}