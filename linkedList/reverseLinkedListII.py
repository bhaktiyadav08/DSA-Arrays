
left=2
right=4
class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
head=Node(1)
node2=Node(2)
node3=Node(3)
node4=Node(4)
node5=Node(5)
head.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
def reverseLinkedListTwo(head,left,right):
    curr=head
    before_left=dummy
    for _ in range(left-1):
        curr=curr.next
    before_left=curr
    org_left=curr.next
    prev=None
    curr=org_left
    j=left
    while j<=right:
        next_node=curr.next
        curr.next=prev
        prev=curr
        curr=next_node
        j+=1
    before_left.next=prev
    org_left.next=curr
    curr=head
    while curr!=None:
        print(curr.val,end='->')
        curr=curr.next
    print(None)  
reverseLinkedListTwo(head,left,right)