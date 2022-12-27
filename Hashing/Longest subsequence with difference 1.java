
import java.util.*;
import java.lang.*;
import java.io.*;

class Accio {
    public int longestSubsequence(int[] nums) {
        int n = nums.length;
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        int maximum = 0;

        for (int i = 0; i < n; i++)
        {
            int len = 0;
            if (map.containsKey(nums[i] - 1) && len < map.get(nums[i] - 1)) {
                  len = map.get(nums[i] - 1);
            } 
            if (map.containsKey(nums[i] + 1) && len < map.get(nums[i] + 1)) {
                  len = map.get(nums[i] + 1);
            }

            map.put(nums[i], len + 1);

            if (maximum < map.get(nums[i])) {
                maximum = map.get(nums[i]);
            }
        }
        return maximum;
    }
}


public class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		//your code here
                Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] nums = new int[N];
    	for(int i=0;i<N;i++)
	    nums[i] = sc.nextInt();
        Accio Obj = new Accio();
        System.out.println(Obj.longestSubsequence(nums));
	}
}
