class Node():
    def __init__(self, value=None, next = None):
        self.value = value
        self.next = next 

class LinkedList():
    def __init__(self):
        self.head= None
    
    def append(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else: # self.head is not None
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode

    def get(self, search_value):
        current = self.head
        while current != None:
            if current == search_value:
                return current 
            current = current.next

    def insert(self, value, insert_value):
        # get position
        current = self.head
        while current != None:
            if current.value == insert_value:
                update_node = current
                print('found', update_node.value)
            current = current.next
        #################

        newNode = Node(value, update_node.next) # 3.5, 4
        update_node.next = newNode
        



    def print(self):
        current = self.head
        while current != None:
            print(current.value)
            current = current.next
    

LL = LinkedList()
LL.append(3)
LL.append(4)
LL.append(5)
LL.append(6)

LL.print()

LL.insert(3.5, 3)

LL.print()
