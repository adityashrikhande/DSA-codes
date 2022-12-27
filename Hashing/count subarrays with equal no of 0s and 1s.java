import java.util.*;

class Solution {
    static int countEqualSubarray01(int arr[], int n)
    {
        //Write your code here
        Map<Integer, Integer> myMap = new HashMap<>();
        int sum = 0;
        int count = 0;
		if(n == 1)return 0;
		
        for (int i = 0; i < n; i++) {
            // Replacing 0's in array with -1
            if (arr[i] == 0)
                arr[i] = -1;
 
            sum += arr[i];
 
            // If sum = 0, it implies number of 0's and 1's
            // are equal from arr[0]..arr[i]
            if (sum == 0)
                count++;
 
            if (myMap.containsKey(sum))
                count += myMap.get(sum);
 
            if (!myMap.containsKey(sum))
                myMap.put(sum, 1);
            else
                myMap.put(sum, myMap.get(sum) + 1);
        }
        return count;
    }   

}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N= sc.nextInt();
    

        int arr[] = new int[N];

        for(int i=0; i<N; i++){
            arr[i]= sc.nextInt();
        }
        
        //Solution Obj = new Solution();
        System.out.println(Solution.countEqualSubarray01(arr,N));
        sc.close();
    }
}