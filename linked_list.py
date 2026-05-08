class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList():
    
    # creating empty linked list
    # property of the empty linked list is the head is none.
    def __init__(self):
        self.head = None # head
        self.n = 0 # number of node 

    def __len__(self):
        return self.n
    
    # Insert operation is three case : from head / from tail and middle : 
    
    # 1. Insert in the Head, we just assign the new head address or next is the previous or last head. 
    def insert_head(self, value):

        # new node
        new_node = Node(value=value)

        # create connection 
        new_node.next = self.head

        # assigning to the head
        self.head = new_node

        self.n = self.n + 1 
        



if __name__ == "__main__":
    # a = Node(1)
    # print(a)
    # print(int(0x000001999B466190))
    # b = Node(2)
    # c = Node(3)
    L = LinkedList()
    print(L)
