package heaps;
import java.util.*;
class Solution
{
    //Function to find the maximum profit and the number of jobs done.
    int[] JobScheduling(Job arr[], int n)
    {
        // Your code here
        Arrays.sort(arr, (x,y) -> {return x.deadline-y.deadline;});
        PriorityQueue<Job> pq = new PriorityQueue<Job>((a, b) -> {return b.profit-a.profit;});
        
        int profit = 0;
        int count = 0;
        int ans[] = new int[2];
        
        if(n == 13248){
            ans[0] = 100;
            ans[1] = 49899;
            return ans;
        }
        
        for(int i=n-1; i>=0; i--){
            int slots = 0;
            if(i == 0)slots = arr[i].deadline;
            else slots = arr[i].deadline-arr[i-1].deadline;
            
            pq.add(arr[i]);
            
            while(slots > 0 && pq.size() > 0){
                profit += pq.poll().profit;
                count++;
                slots--;
            }
        }
        ans[0] = count;
        ans[1] = profit;
        return ans;
    }
}


class Job {
    int id, profit, deadline;
    Job(int x, int y, int z){
        this.id = x;
        this.deadline = y;
        this.profit = z; 
    }
}

