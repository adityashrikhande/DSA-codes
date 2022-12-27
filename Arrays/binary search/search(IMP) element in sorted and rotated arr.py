
def search(arr, target) :
    # Write your code here.
    low = 0
    high = len(arr)-1
    
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        if arr[mid] >= arr[low]:
            if arr[low] <= target and arr[mid] >= target:
                high = mid-1
            else:
                low = mid+1
        else:
            if arr[high] >= target and arr[mid] <= target:
                low = mid+1
            else:
                high = mid-1
    return -1

# java iterative approach
# import java.util.*;
# import java.lang.*;
# import java.io.*;

# public class Main
# {

#         public static int BinarySearch(int[] arr, int low, int high, int target){
#                 if(low > high)return -1;

#                 while(low <= high){
#                         int mid = (low + high)/2;
#                         if(target == arr[mid])return mid;
                        
#                         if(arr[mid] >= arr[low]){
#                                 if(arr[low] <= target && arr[mid] >= target){
#                                         high = mid-1;
#                                 }else{
#                                         low = mid+1;
#                                 }
#                         }else{
#                                 if(arr[mid] <= target && arr[high] >= target){
#                                         low = mid+1;
#                                 }else{
#                                         high = mid-1;
#                                 }
#                         }
#                 }
#                 return -1;
#         }
        
# 	public static void main (String[] args) throws java.lang.Exception
# 	{
# 		//your code here
#                 Scanner sc = new Scanner(System.in);
#                 int n = sc.nextInt();
#                 int arr[] = new int[n];
#                 for(int i=0; i<n; i++){
#                         arr[i] = sc.nextInt();
#                 }
#                 int target = sc.nextInt();
#                 //int pivot = -1;
#                 int targetIdx = -1;

#                 targetIdx = BinarySearch(arr, 0, n-1, target);
                
#                 System.out.println(targetIdx);
# 	}
# }


# java code pivot approach     
# 
# import java.util.*;
# import java.lang.*;
# import java.io.*;

# public class Main
# {

#         public static int Pivot(int[] arr, int low, int high){
                
#                 if(low > high)return -1;
#                 if(high == low)return low;

#                 int mid = (low+high)/2;

#                 if(low < mid && arr[mid] < arr[mid-1]){
#                         return mid-1;
#                 }
#                 if(high > mid && arr[mid] > arr[mid+1]){
#                         return mid;
#                 }
#                 if(arr[mid] > arr[low]){
#                         return Pivot(arr, mid+1, high);
#                 }
#                 return Pivot(arr, low, mid-1);
                
#         }

#         public static int BinarySearch(int[] arr, int low, int high, int target){
#                 if(low > high)return -1;

#                 int mid = (low + high)/2;
#                 if(target == arr[mid])return mid;
                
#                 if(arr[mid] > target){
#                         return BinarySearch(arr, low, mid-1, target);
#                 }else{
#                         return BinarySearch(arr, mid+1, high, target);
#                 }
#         }
        
# 	public static void main (String[] args) throws java.lang.Exception
# 	{
# 		//your code here
#                 Scanner sc = new Scanner(System.in);
#                 int n = sc.nextInt();
#                 int arr[] = new int[n];
#                 for(int i=0; i<n; i++){
#                         arr[i] = sc.nextInt();
#                 }
#                 int target = sc.nextInt();
#                 int pivot = -1;
#                 int targetIdx = -1;
#                 pivot = Pivot(arr, 0, n-1);
#                 if(arr[pivot] == target){
#                         System.out.println(pivot);
#                         return;
#                 }
                
#                 if(pivot == -1){
#                         targetIdx = BinarySearch(arr, 0, n-1, target);
#                 }else{
#                         targetIdx = BinarySearch(arr, pivot+1, n-1, target);
#                         if(targetIdx == -1){
#                                 targetIdx = BinarySearch(arr, 0, pivot, target);
#                         }
#                 }
#                 System.out.println(targetIdx);
# 	}
# }  