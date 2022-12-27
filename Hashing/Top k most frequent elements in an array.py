
class Solution:
	def topK(self, nums, k):
		
		n = len(nums)
		ans = []
		kc = 0
		d = dict()
		
		for i in range(n):
			if nums[i] in d.keys():
				d[nums[i]] += 1
			else:
				d[nums[i]] = 1
		
		dic = sorted(d.items(), key = lambda x: x[0], reverse = True)
		
		l = [[] for i in range(n+1)]
		
		for i in dic:
		    l[i[1]].append(i[0])
				
		for i in range(n, 0, -1):
			for j in l[i]:
				ans.append(j)
				kc += 1
				if kc == k:
					return ans
		
		
		        
