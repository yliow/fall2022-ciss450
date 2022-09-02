class SLNode:
    def __init__(self, key, next_=None):
        self.__key = key
        self.__next = next_
    def get_key(self):
        return self.__key
    key = property(get_key, None)
    
class SLList:
    def __init__(self):
        self.__head = None
        
    def __str__(self):
        return "<SLList []>"
    
#node = SLNode(42)
#print(node.key)
