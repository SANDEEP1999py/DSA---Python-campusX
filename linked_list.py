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
    
    def print_head(self):
        if self.head == None:
            return "please assign head of LL"
        return self.head.data
        
    # Insert operation is three case : from head / from tail and middle : 
    
    # 1. Insert in the Head, we just assign the new head address or next is the previous or last head. 
    def insert_head(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            return
        new_node.next = self.head
        self.head = new_node
        self.n = self.n + 1
        return 

    def traverse(self):
        len_self = self.n
        result = ''
        head_dummy = self.head
        for i in range(len_self):
            if head_dummy != None:
                num = head_dummy.data
                result = ' ->' + str(num) + result
                head_dummy = head_dummy.next
        return result[3:]
    
    def insert_tail(self, value):
        # print(f"Inerting Tail function with total len of LL is {self.n}")
        # print(f"The head value is {self.head.data}")
        len_num = self.n
        dummy_head = self.head
        new_node = Node(value)
        for i in range(len_num):
            # print(f"loop starts with value of i is {i}")
            # print(f"dummy head value is {dummy_head.data}")
            if dummy_head.next == None:
                # print(f"condition satisfy with value of i is {i}")
                dummy_head.next = new_node
                self.n = self.n + 1
                return
            dummy_head = dummy_head.next

    def insert_at_position(self, value, pos):
        if 0 < pos < self.n:
            new_node = Node(value)
            len_ = self.n
            dummy_head = self.head
            for i in range(self.n):
                if i == pos - 2:
                    new_node.next = dummy_head.next
                    dummy_head.next = new_node
                    self.n = self.n + 1
                    return
                dummy_head = dummy_head.next
        elif pos == self.n:
            self.insert_tail(value)
            return
        elif pos == 0:
            self.insert_head(value)
            return
        else:
            raise "please give valid input"

        
    def delete_head(self):
        if self.head != None:
            self.head = self.head.next
            self.n = self.n - 1
            return
        return print("The Linklist is empty")
    
    def delete_tail(self):
        dummy_head = self.head
        for i in range(self.n):    
            if dummy_head.next.next == None:
                dummy_head.next = None
                self.n = self.n - 1
                return
            dummy_head = dummy_head.next
    
    def find_pos(self, value):
        dummy_head = self.head
        if self.head.data == value:
            return 1
        for i in range(self.n):
            if dummy_head.next.data == value:
                pos = i + 2
                return pos
            dummy_head = dummy_head.next
    
    def remove_val(self, value):
        dummy_head = self.head
        for i in range(self.n):
            if dummy_head.next.data == value:
                dummy_head.next = dummy_head.next.next
                self.n = self.n - 1
                return
            dummy_head = dummy_head.next
                

        
if __name__ == "__main__":
    # a = Node(1)
    # print(a)
    # print(int(0x000001999B466190))
    # b = Node(2)
    # c = Node(3)
    L = LinkedList()
    L.insert_head(15)
    L.insert_head(10)
    L.insert_head(10)
    L.insert_head(5)
    print("-----------------------------")
    result_ = L.traverse()
    print(result_)
    print("-----------------------------")
    L.insert_tail(20)
    print(len(L))
    print("-----------------------------")
    result_ = L.traverse()
    print(result_)
    print("-----------------------------")
    print("-----------------------------")
    L.insert_at_position(value=29,pos=0)
    L.insert_at_position(value=00,pos=len(L))
    L.insert_at_position(value=78, pos=3)
    result_ = L.traverse()
    print(result_)
    print("-----------------------------")
    L.delete_head()
    L.delete_tail()
    result_ = L.traverse()
    print(result_)
    print(L.find_pos(15))
    print("-----------------------------")
    print(L.remove_val(15))
    result_ = L.traverse()
    print(result_)
    print("-----------------------------")
    # L.insert_head(20)
    
    # print(L.print_head())
    # print(len(L))
    # print(L.traverse())
    # L.insert_tail(6)
    # print(L.traverse())