# your task is to complete this Function
# Function shouldn't return anything

'''
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def skipMdeleteN(self, head, M, N):
        
        curr = head
          
        # The main loop that traverses through the
        # whole list
        while(curr):
            # Skip M nodes
            for count in range(1, M):
                if curr is None:
                    return 
                curr = curr.next
                      
            if curr is None :
                return 
  
            # Start from next node and delete N nodes
            t = curr.next 
            for count in range(1, N+1):
                if t is None:
                    break
                t = t.next
      
            # Link the previous list with remaining nodes
            curr.next = t
            # Set Current pointer for next iteration
            curr = t 
        
        return head
            
        


#{ 
 # Driver Code Starts
#main

class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to prit the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ") 
            temp = temp.next
        print("")


if __name__=='__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = int(input())
        m,p = list(map(int, input().strip().split()))
        values = input().strip().split()
        for i in reversed(values):
            llist.push(i)
        Solution().skipMdeleteN(llist.head, m, p)
        llist.printList()
        t -= 1
# Contributed by: Harshit Sidhwa
# } Driver Code Ends