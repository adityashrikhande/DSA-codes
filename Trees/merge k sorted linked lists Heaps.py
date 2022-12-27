
# python code

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from queue import PriorityQueue

class Solution:
    def mergeKLists(self, A):
        
        q = PriorityQueue()
        
        head = temp = ListNode(0)

        for l in A:
            if l:
                q.put((l.val, l))
        
        while not q.empty():
            
            val, node = q.get()
            temp.next = ListNode(val)
            temp = temp.next
            node = node.next
            if node:
                q.put((node.val, node))
            
        return head.next
        
"""
# cpp code

#include<bits/stdc++.h> 
using namespace std;

ListNode* Solution::mergeKLists(vector<ListNode*> &A) {
    
    priority_queue<pair<int, ListNode*>, vector<pair<int, ListNode*>>, greater<pair<int, ListNode*>>> pq;
    
    ListNode* head = new ListNode(0);
    ListNode* temp = head;
    
    for (int i=0; i<A.size(); i++) {
        
        if (A[i] != NULL){
            pq.push({A[i]->val, A[i]});
        }
    }
    
    while(!pq.empty()){
        
        pair<int, ListNode*> p = pq.top();
        pq.pop();
        int val = p.first;
        ListNode* node = p.second;
        node = node->next;
        temp->next = new ListNode(val);
        temp = temp->next;
        if (node != NULL){
            pq.push({node->val, node});
        }
    }
    
    return head->next;    
}
"""
