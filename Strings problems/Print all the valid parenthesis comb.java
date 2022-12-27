
public class Main
{

    static void printParenthesis(char str[], int pos, int n, int open, int close)                             
    {
        if (close == n) {
            // print the possible combinations
            for (int i = 0; i < str.length; i++)
                System.out.print(str[i]);
            System.out.println();
            return;
        }
        else {
            if (open < n) {
                str[pos] = '(';
                printParenthesis(str, pos + 1, n, open + 1,close);                        
            }
            if (open > close) {
                str[pos] = ')';
                printParenthesis(str, pos + 1, n, open, close + 1);                       
            }
            
        }
    }
               
	public static void main (String[] args) throws java.lang.Exception
	{
		//your code here
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        char str[] = new char[2*n];
        printParenthesis(str,  0, n,  0, 0);
	}
}