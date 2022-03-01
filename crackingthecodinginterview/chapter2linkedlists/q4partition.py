#q2.4 from cracking the coding interview
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

def partition(ll,partition):
    if ll:
        cur=head=tail=ll
        while cur:
            nxt=cur.next
            cur.next=None
            if cur.data<partition:
                cur.next=head
                head=cur
            else:
                tail.next=cur
                tail=cur
            cur=nxt
        #break loop when there is no or only one element that is bigger than the partition
        if tail.next:
            tail.next=None
        return head

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
def print_list(ll):
        cur_node=ll
        while cur_node:
            print(cur_node.data)
            cur_node=cur_node.next
if __name__ == "__main__":
    #ll1 = createLinkedList([3,5,8,10,2])
    ll1 = createLinkedList([6,8])
    print("before")
    print_list(ll1)
    output_1 = partition(ll1,5)
    print("after")
    print_list(output_1)