#Reverse Operations from Facebook preparation question
#Example
#Input:
#N = 6
#list = [1, 2, 8, 9, 12, 16]
#Output:
#[1, 8, 2, 9, 16, 12]#

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Add any helper functions you may need here
 
def reverse_parts(start,first,last,after):
    start=start
    prev=first
    cur=prev.next
    while cur!=after:
        nxt=cur.next
        cur.next=prev
        #prev.next=nxt
        prev=cur
        cur=nxt
    start.next=last
    first.next=after
    
def reverse(head):
    # Write your code here
    dummy=Node(None)
    dummy.next=head
    cur=first=dummy
    #one node
    last=first.next
    #border
    after=cur.next
    prev=None
    while after:
        if after.data%2==1: #odd
            if first!=dummy:

                last=cur
                reverse_parts(prev,first,last,after)
                first=dummy
        else:
            if (first==dummy) or (first.data%2==1): 
                prev=cur
                first=after
        cur=after
        after=after.next
    if first==dummy:
        return dummy.next
    elif first and first.data%2==0: #last is border
        last=cur
        reverse_parts(prev,first,last,after)
    return dummy.next
def createLinkedList(arr):
    head = None
    tempHead = head
    for v in arr:
        if head == None:
            head = Node(v)
            tempHead = head
        else:
            head.next = Node(v)
            head = head.next
    return tempHead
if __name__ == "__main__":
    head_1 = createLinkedList([1, 2, 8, 9, 12, 16])
    expected_1 = createLinkedList([1, 8, 2, 9, 16, 12])
    output_1 = reverse(head_1)
    #check(expected_1, output_1)

    head_2 = createLinkedList([2, 18, 24, 3, 5, 7, 9, 6, 12,5])
    expected_2 = createLinkedList([24, 18, 2, 3, 5, 7, 9, 12, 6,5])
    output_2 = reverse(head_2)
    print("2")
    #check(expected_2, output_2)