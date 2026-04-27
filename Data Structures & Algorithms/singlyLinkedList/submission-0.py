class SinglyNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def display(self):
        cur = self.head
        elements = []
        while cur:
            elements.append(str(cur.val))
            cur = cur.next
        elements.append('None')
        return ' -> '.join(elements)
    def get(self, index: int) -> int:
        cur = self.head
        i = 0
        while cur:
            if i == index:
                return cur.val
            cur = cur.next
            i += 1
        return  -1                                    
    def insertHead(self, val: int) -> None:
        head_node = SinglyNode(val)
        head_node.next = self.head
        self.head = head_node
    def insertTail(self, val: int) -> None:
        tail_node =  SinglyNode(val)
        if not self.head:
            self.head = tail_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = tail_node
    def remove(self, index: int) -> bool:
        if not self.head: return False
        if index == 0:
            self.head = self.head.next
            return True
        cur = self.head
        i = 0
        while cur and cur.next:
            if i+1 == index:
                cur.next = cur.next.next
                return True
            cur = cur.next
            i += 1
        return False
    def getValues(self) -> List[int]:
        values = []
        cur = self.head
        while cur:
            values.append(cur.val)
            cur = cur.next
        return values
        
