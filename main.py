
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
n3.next_node(None)

current_node = n1

while True:
    print(current_node)
    current_node = current_node.next