import java.util.*;
//import java.lang.*;
//import java.io.*;

class Main
{
        public static int prec(char a){
                if(a == '^'){
                        return 3;
                }else if(a == '*' || a == '/'){
                        return 2;
                }else if(a == '+' || a == '-'){
                        return 1;
                }else{
                        return -1;
                }
        }
        
	public static void main (String[] args) throws java.lang.Exception
	{
		//your code here
                Scanner sc = new Scanner(System.in);
                String s = sc.next();
                int n = s.length();
                Deque<Character> st = new ArrayDeque<Character>();
                String ans = "";
                
                for(int i=0; i<n; i++){
                        if((s.charAt(i) >= 'A' && s.charAt(i)<= 'Z') || (s.charAt(i) >= 'a' && s.charAt(i)<= 'z')){
                                ans += s.charAt(i);
                        }else if(s.charAt(i) == '('){
                                st.push('(');
                        }else if(s.charAt(i) == ')'){
                                while(!st.isEmpty() && st.peek() != '('){
                                        ans += st.pop();
                                }
                                if(!st.isEmpty()){
                                        st.pop();
                                }
                        }else{
                                while(!st.isEmpty() && (prec( st.peek()) >= prec( s.charAt(i)))){
                                        ans += st.pop();
                                }
                                st.push(s.charAt(i));
                        }
                }
                while (!st.isEmpty()){
                        ans += st.pop();
                }
                sc.close();
                
                System.out.println(ans);
	}
}