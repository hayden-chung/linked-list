
class Node():
    def __init__(self, value):
        self.value = value
        self.next = self

    def __str__(self):
        #print(self.value)
        return str(self.value)

test = Node('aoiseufa')
print(test.value)

nodes = []
# for i in range(10):
#     n = Node(i)
#     nodes.append(n)
# print(nodes)

# for n in nodes:
#     print(n)


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
list = [n1, n2, n3]

print(n1, n2, n3)
print(n1.next)