
# O(n3 * log n) comp

class Solution:
    def fourSum(self, arr, k):
        # code here
        
        arr.sort()
        n = len(arr)
        ans = []
        
        for i in range(n-3):
            
            if (arr[i] > 0 and arr[i] > k):
                break
            # removing duplicates
            if (i > 0 and arr[i] == arr[i - 1]):
                continue
            
            for j in range(i+1,n-2):
                
                if (j > i + 1 and arr[j] == arr[j - 1]):
                    continue
                
                k1 = j + 1
                l = n - 1
                
                while k1 < l:
                    ok = k1
                    ol = l
                    if (arr[i] + arr[j] + arr[k1] + arr[l]) == k:
                        li = [arr[i], arr[j], arr[k1], arr[l]]
                        li.sort()
                        ans.append(li)
                        
                        while k1 < l and arr[k1] == arr[ok]:
                            k1 += 1
                            
                        while k1 < l and arr[l] == arr[ol]:
                            l -= 1
                        
                    elif (arr[i] + arr[j] + arr[k1] + arr[l]) < k:
                        k1 += 1
                    else:
                        l -= 1
                 
        #ans.sort()                
        return ans