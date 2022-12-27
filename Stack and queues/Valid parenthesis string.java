
import java.util.*;

class Solution{
    public static boolean checkValidString(int n, String s){
        //write code here
		Stack<Integer> left = new Stack<>();
		Stack<Integer> star = new Stack<>();

		for(int i=0; i<n; i++){
			if(s.charAt(i) == '('){
				left.add(i);
			}else if(s.charAt(i) == '*'){
				star.add(i);
			}else{
				if(left.isEmpty() && star.isEmpty())return false;
				else if(!left.isEmpty())left.pop();
				else star.pop();
			}
		}
		while(!left.isEmpty() && !star.isEmpty()){
			if(left.pop() > star.pop())return false;
		}
		return left.isEmpty();
    }
}

public class Main {
    public static void main(String[] args) throws Throwable {
        Scanner sc = new Scanner(System.in);
        int n;
        n = sc.nextInt();
        String s = sc.nextLine();
		s += sc.nextLine();
        Solution obj = new Solution();
        boolean ans = obj.checkValidString(n,s);
        if(ans==true){
            System.out.println("true");
        }else{
            System.out.println("false");
        }
    }
}