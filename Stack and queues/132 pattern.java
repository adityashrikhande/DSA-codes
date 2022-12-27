
import java.util.*;

class Solution {
    public boolean find132pattern(int[] nums) {
        //Write code here
		int n = nums.length;
		Stack<Integer> st = new Stack<>();
		int s3 = Integer.MIN_VALUE;
		for(int i=n-1; i>=0; i--){
			if(nums[i] < s3)return true;
			while(!st.isEmpty() && nums[i] > st.peek()){
				s3 = st.pop();
			}
			st.push(nums[i]);
		}
		return false;
    }
}

