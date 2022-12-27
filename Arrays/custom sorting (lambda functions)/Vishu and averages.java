import java.util.*;
//import java.lang.*;
//import java.io.*;

class Main // (x.get(0) > y.get(0) || (x.get(0) == y.get(0) && x.get(1) < y.get(1)) ? 1 : -1));
{
	public static void main (String[] args) throws java.lang.Exception
	{
		//your code here
                Scanner sc = new Scanner(System.in);
                int n = sc.nextInt();
                ArrayList<ArrayList<Integer>> records = new ArrayList<ArrayList<Integer>>();

                for(int i=0; i<n; i++){
                        records.add(new ArrayList<Integer>());
                        records.get(i).add(sc.nextInt());
                        records.get(i).add(sc.nextInt());
                }
                sc.close();
                Collections.sort(records, (x, y) -> 
                        {
                                if(x.get(0) > y.get(0))
                                         return 1;
                                else if(x.get(0) == y.get(0) && x.get(1) < y.get(1)){
                                        return 1;
                                }else{
                                        return -1;
                                }
                        });
                int id = -1;
                for(int i=0; i<n; i++){
                        if(id != records.get(i).get(0)){
                                int sum = 0;
                                for(int j=i; j<5+i; j++){
                                        sum += records.get(j).get(1);
                                }
                                id = records.get(i).get(0);
                                if(i == n-1){
                                        System.out.println(id + " " + sum/5);
                                }
                                System.out.println(id + " " + sum/5 + " ");
                        }
                }
	}
}
