
class Node():
    def __init__(self, value):
        print('called init function')
        self.value = value
        self.next = None

    def __str__(self):
        #print(self.value)
        return str(self.value)

    def next_node (self, node):
        self.next = node

n1 = Node('a')
n2 = Node('b')
n3 = Node('c')
n1.next_node(n2)
n2.next_node(n3)

current_node = n1

def print_all(head):
    while True:
        print(head)
        if head.next == None:
            break
        head = head.next

print_all(current_node)

def append(head, node):
    current = head 
    while True: 
        if current.next == None:
            break 
        current = current.next

    current.next = node

n4 = Node('d')
n4 = append(current_node, n4)
print_all(current_node)