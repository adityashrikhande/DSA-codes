import java.util.*;
import java.lang.*;
import java.io.*;

public class Main
{

    public static int Partition(int[] arr, int low, int high){
        int pivot = arr[high];
        int i = low-1;
        for(int j=low; j<high; j++){
            if(arr[j] < pivot){
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        int temp = arr[i+1];
        arr[i+1] = arr[high];
        arr[high] = temp;
        
        return i+1;
}

    public static void QuickSort(int[] arr, int l, int r){
        if(l<r){
            int pivot = Partition(arr, l, r);
            QuickSort(arr, l, pivot-1);
            QuickSort(arr, pivot+1, r);
        }
    }
        
	public static void main (String[] args) throws java.lang.Exception
	{
		//your code here
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int arr[] = new int[n];
        for(int i=0; i<n; i++){
            arr[i] = sc.nextInt();
        }
        QuickSort(arr, 0, n-1);
        for(int i=0; i<n; i++){
            System.out.print(arr[i] + " ");
        }
	}
}

