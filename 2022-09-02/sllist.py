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
