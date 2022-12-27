import java.util.*;

class Accio {

	public int atmost(int[] arr, int b, int n){
		int left = 0;
		int right = 0;
		int count = 0;

		HashMap<Integer, Integer> mp = new HashMap<>();
		while(right < n){
			mp.put(arr[right], mp.getOrDefault(arr[right], 0)+1);

			while(mp.size() > b){
				mp.put(arr[left], mp.get(arr[left])-1);
				if(mp.get(arr[left]) == 0){
					mp.remove(arr[left]);
				}
				left++;
			}
			count += right-left+1;
			right++;
		}
		return count;
	}
	
    public int solve(int[] a, int b) {
        //Your code goes here
		int n = a.length;
		
		return atmost(a, b, n)-atmost(a, b-1, n);
    }
}

class Main {  
  public static void main (String[] args)
	{
		Scanner sc = new Scanner(System.in);
	    
	    int n = sc.nextInt();
		int[] a = new int[n];
    	for(int i=0;i<n;i++)
		{
			a[i] = sc.nextInt();
		}
		int b = sc.nextInt();
		Accio Obj = new Accio();
        System.out.println(Obj.solve(a, b));
        sc.close();
	}
}
