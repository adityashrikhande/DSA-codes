
class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):

        li = ["a","e","i","o","u"]
        n = len(A)
        cnt = 0
        cnt2 = 0
        ans = 0

        vovel_pre = [0]*n
        conso_pre = [0]*n

        for i in range(n-1,-1,-1):
            if A[i] in li:
                cnt += 1
                vovel_pre[i] = cnt
            else:
                vovel_pre[i] = cnt
            
            if A[i] not in li:
                cnt2 += 1
                conso_pre[i] = cnt2
            else:
                conso_pre[i] = cnt2

        for i in range(n-1):
            
            if A[i] in li:
                ans += conso_pre[i]
            else:
                ans += vovel_pre[i]

        return int(ans%(1e9+7))
            
        




