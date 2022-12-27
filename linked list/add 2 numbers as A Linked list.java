

// node for linked list

class Node {
    int data;
    Node next;

    Node(int d) {
        data = d;
        next = null;
    }
}

// 

class Solution{
    
    static Node reverse(Node head){
        Node prev = null;
        Node cur = head;
        Node nex = head;
        
        while (nex != null){
            nex = cur.next;
            cur.next = prev;
            prev = cur;
            cur = nex;
        }
        return prev;
    }
    //Function to add two numbers represented by linked list.
    static Node addTwoLists(Node first, Node second){
        // code here
        // return head of sum list
        
        first = reverse(first);
        second = reverse(second);
        
        Node head1 = first;
        Node head2 = second;
        int carry = 0;
        Node head = null;
        
        while(head1 != null || head2 != null || carry > 0){
            
            int sum = 0;
            if(head1 != null)sum += head1.data;
            if(head2 != null)sum += head2.data;
            sum += carry;
            
            Node temp = new Node(sum%10);
            temp.next = head;
            
            carry = sum/10;
            
            head = temp;
            
            if(head1 != null)
                head1 = head1.next;
            if(head2 != null)
                head2 = head2.next;
            
        }
        
        return head;
        
    }
}
