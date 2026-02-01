class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None
    
def addTwoNumbers(l1,l2):
    head1=l1
    head2=l2
    l3=ListNode(None)
    current=l3
    carry, digit = 0, 0
    while head1!=None or head2!=None:
        x=head1.data if head1 else 0
        y=head2.data if head2 else 0
        sum=x+y+carry
        digit=sum%10
        carry=sum//10
        current.next=ListNode(digit)
        if head1:  
         head1=head1.next
        if head2:
         head2=head2.next
        current=current.next
    if carry>0:
       current.next=ListNode(carry)
    return l3.next
l1=ListNode(9)
l1.next=ListNode(9)
l1.next.next=ListNode(9)
l1.next.next.next=ListNode(9)
l1.next.next.next.next=ListNode(9)
l1.next.next.next.next.next=ListNode(9)
l1.next.next.next.next.next.next=ListNode(9)
l2=ListNode(9)
l2.next=ListNode(9)
l2.next.next=ListNode(9)
l2.next.next.next=ListNode(9)
def printList(head):
   while head:
      print(head.data,end="->")
      head=head.next
   print("None")
result=addTwoNumbers(l1,l2)
printList(result)
