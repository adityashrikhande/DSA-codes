
from typing import List

def subsum(idx, num, li, sum):
    if idx < 0:
        li.append(sum)
        return
    subsum(idx-1, num, li, sum)
    subsum(idx-1, num, li, sum + num[idx])
    return

def subsetSum(num: List[int]) -> List[int]:
    # Write your code here.
    n = len(num)
    li = []
    subsum(n-1, num, li, 0)
    li.sort()
    
    return li