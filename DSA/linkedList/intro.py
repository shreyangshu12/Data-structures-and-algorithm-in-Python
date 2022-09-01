class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        
class linkedlist:
    def __init__(self):
        self.head=None
        
    #fun to print the linkedlist
    def print_linkedlist(self):
        tmp=self.head
        while(tmp):
            print(tmp.data)
            tmp=tmp.next
      
    #fun to add elements to the begining of the linkedlist --O(1)     
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    #fun to add elements to the end of the linkedlist --O(n) 
    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while (last.next):
            last = last.next
            
        last.next = new_node

    #fun to insert elements after certain node        
    def insertAfter(self, prev_node, new_data):
        # 1. check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return
    
        # 2. Create new node &
        # 3. Put in the data
        new_node = Node(new_data)
    
        # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next
    
        # 5. make next of prev_node as new_node
        prev_node.next = new_node
        
    def deleteNode(self, key):
     
        # Store head node
        temp = self.head
 
        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
 
        # Search for the key to be deleted, keep track of the previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
 
        # if key was not present in linked list
        if(temp == None):
            return
 
        # Unlink the node from linked list
        prev.next = temp.next
 
        temp = None
                
                
            
if __name__ ==  '__main__':
    
    # Start with the empty list
    a = linkedlist()
 
    a.head = Node(1)
    second = Node(2)
    third  = Node(3)
 
    a.head.next = second  # Link first node with second
    second.next = third   # Link second node with the third node
 
    a.insert_at_beginning(8)
    a.insert_at_end(34)
    a.insertAfter(second,89)
    a.deleteNode(8)
    a.print_linkedlist()