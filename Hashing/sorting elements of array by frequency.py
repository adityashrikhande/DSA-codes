
# cpp solution custom comparator

#include<bits/stdc++.h>

"""class Solution {
public:
    
    
    vector<int> frequencySort(vector<int>& nums) {
        
        int n = nums.size();
        map<int,int> mp;
        
        for(int i=0; i<n; i++){
            mp[nums[i]]++;
        }
        
        sort(nums.begin(), nums.end(), [&](int a, int b){ return mp[a] != mp[b] ? mp[a] < mp[b] : a > b;});
        
       
        return nums;
        
    }
};
"""
# sorting by freq: larger freq elements come first and if equal smaller element comes first  gfg

class Solution:
   
    #Function to sort the array according to frequency of elements.
    def sortByFreq(self,a,n):
        
        dic = dict()
        
        ans = []
        
        for i in range(n):
            
            if a[i] in dic.keys():
                dic[a[i]] += 1
            else:
                dic[a[i]] = 1
        
        freq = [[] for i in range(n+1)]
        
        d = sorted(dic.items(), key = lambda x:x[0], reverse = False) # sorting by keys x[0]
        
        for i in d:
            freq[i[1]].append(i[0])
            
        for i in range(n, 0, -1):
            
            for j in freq[i]:
                
                for k in range(i):
                    ans.append(j)
        
        return ans


# sorting by freq: smaller freq elements come first and if equal larger element comes first leetcode

class Solution:
    def frequencySort(self, a: list[int]) -> list[int]:
        dic = dict()
        n = len(a)
        ans = []
        
        for i in range(n):
            
            if a[i] in dic.keys():
                dic[a[i]] += 1
            else:
                dic[a[i]] = 1
        
        freq = [[] for i in range(n+1)]
        
        d = sorted(dic.items(), key = lambda x:x[0], reverse = True) # sorting by keys x[0]
        
        for i in d:
            freq[i[1]].append(i[0])
            
        for i in range(1, n+1):
            
            for j in freq[i]:
                
                for k in range(i):
                    ans.append(j)
        
        return ans
        
        
        