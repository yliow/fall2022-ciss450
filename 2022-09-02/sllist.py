class SLNode:
    def __init__(self, key, next_=None):
        self.__key = key
        self.__next = next_
    def get_key(self):
        return self.__key
    key = property(get_key, None)
    def get_next(self):
        return self.__next
    next_node = property(get_next, None)
    
class SLList:
    def __init__(self):
        self.__head = None        
    def insert_head(self, key):
        self.__head = SLNode(key, self.__head)
    def delete_head(self):
        """ No underflow exception thrown """
        if self.__head != None:
            self.__head = self.__head.next_node
            # NOTE: There's no mem leak because of garbage collector
    def get_head_key(self):
        """ No underflow exeption thrown """
        if self.__head != None:
            return self.__head.key
    head = property(get_head_key, None)
    def __str__(self):
        node = self.__head
        xs = []
        while node != None:
            xs.append(str(node.key))
            node = node.next_node
        s = ', '.join(xs)
        return "<SLList [%s]>" % s
    
#node = SLNode(42)
#print(node.key)
sllist = SLList()
for x in [42,0,1,6]:
    sllist.insert_head(x)
    print(sllist)

for x in range(10):
    head = sllist.head
    sllist.delete_head()
    print(head, sllist)

sllist = SLList()
for x in range(10):
    sllist.insert_head(list(range(x)))
    print(sllist)
for x in range(10):
    head = sllist.head
    sllist.delete_head()
    print(head, sllist)

# To check for memory leaks, run this program and in another shell run
# 'top' and check the %MEM for memory usage. If there's a memory leak the
# value of %MEM will grow.
input("enter to start mem leaks test ...")
while 1:
    sllist = SLList()
    for x in range(1000000):
        sllist.insert_head(x)
