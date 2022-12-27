
public class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		//your code here
                Scanner sc = new Scanner(System.in);
                int n = sc.nextInt();
                int k = sc.nextInt();
                int arr[] = new int[n];
                for(int i=0; i<n; i++){
                        arr[i] = sc.nextInt();
                }
                HashMap<Integer, Integer> mp = new HashMap<>();
                long sum = 0;
                long ans = 0;
                for(int i=0; i<n; i++){
                        sum += arr[i];
                        if(sum == k){
                                ans = i+1;
                        }
                        if(!mp.containsKey((int)sum)){
                                mp.put((int)sum, i);
                        }
                        if(mp.containsKey((int)(sum-k))){
                                if(ans < i-(mp.get((int)(sum-k)))){
                                        ans = i-(mp.get((int)(sum-k)));
                                }
                        }
                }
                System.out.println(ans);
	}
}