
import java.util.*;
import java.lang.*;
import java.io.*;

public class Main
{

    private static Set<String> dictionary = new HashSet<>();

    public static int wordBreak( String word, String[] st){
        int size = word.length();

        if(size == 0){
            return 1;
        }
        for(int i=1; i<=size; i++){

            if(dictionary.contains(word.substring(0, i))){
                if(wordBreak(word.substring(i, size), st) == 1){
                    return 1;
                }
            }
        }
        return 0;
    }
        
	public static void main (String[] args) throws java.lang.Exception
	{
		//your code here
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String st[] = new String[n];
        for(int i=0; i<n; i++){
            st[i] = sc.next();
        }
        String word = sc.next();
        //int siz = word.length();
        
        // loop to add all strings in dictionary set
        for (String temp :st)
        {
            dictionary.add(temp);
        }

        System.out.println(wordBreak(word, st));
	}
}