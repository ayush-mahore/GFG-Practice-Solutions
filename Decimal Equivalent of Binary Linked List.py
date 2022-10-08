# your task is to complete this function
# Function should return an integer value

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def decimalValue(head):
    MOD=10**9+7
    leni = 0
    itr = head
    while itr :
        leni += 1
        itr = itr.next
    itr = head
    numi, count = 0, 0
    while itr:
        numi += (itr.data)*(2**(leni-count-1))
        count += 1
        itr = itr.next
        
    return (numi)%MOD
    
#{ 
 # Driver Code Starts
# Node Class    
class node:
    def __init__(self):
        self.data = None
        self.next = None
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head == None:
            self.head = node()
            self.head.data = data
        else:
            new_node = node()
            new_node.data = data
            new_node.next = None
            temp = self.head
            while(temp.next):
                temp=temp.next
            temp.next = new_node

# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in values:
            list1.insert(i)
        print(decimalValue(list1.head))
# Contributed By: Harshit Sidhwa
# } Driver Code Ends