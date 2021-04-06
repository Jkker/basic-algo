# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize
        # next as null


# Linked List class
class LinkedList:

    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None

    def traversal(self):
        if not self.head:
            return
        head = self.head
        while head:
            print(head.val, end=' ')
            head = head.next

    def reverse(self):
        # Initialize pointers
        curr = self.head
        prev = None
        while curr:
            # Store next
            nxt = curr.next
            # Reverse next and prev
            curr.next = prev
            # Advance the pointers
            prev = curr
            curr = nxt
        self.head = prev

    def add(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            prev_head = self.head
            self.head = node
            self.head.next = prev_head


def traversal(self):
    if not self:
        return
    head = self
    while head:
        print(head.val, end=' ')
        head = head.next


# def clean(head):
#     if not head or not head.next:
#         return
#     else:
#         if head.next.data == 0:
#             head.next = head.next.next
#             clean(head)
#         else:
#             clean(head.next)
def clean(head):
    if not head:  # Head is None
        return None
    else:
        if head.val == 0:
            return clean(head.next)
        else:
            head.next = clean(head.next)
            return head


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    l_list = LinkedList()
    l_list.add(0)
    l_list.add(1)
    l_list.add(0)
    l_list.add(2)
    l_list.add(0)
    l_list.add(0)
    l_list.add(3)
    l_list.add(0)
    l = l_list.head
    print('Before cleaning: ')
    l_list.traversal()
    print('\nAfter Cleaning')
    clean(l)
    traversal(l)
    # l_list.traversal()
