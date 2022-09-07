from multiprocessing.util import log_to_stderr


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None
        self.tail = None
    
    def find_node_at(self, index):
        iterator = self.head
        for _ in range(index):
            iterator = iterator.next

        return iterator

    def insert_after(self, previous_node, data):
        """링크드 리스트 주어진 노드 위  삽입 연산 메소드"""
        new_node = Node(data)
        if previous_node is self.tail:
            self.tail.next = new_node
            self.tail=  new_node
        else:
            temp = previous_node.next
            previous_node.next = new_node
            new_node.next = temp



    """링크드 리스트 추가 연산 메소드"""
    def append(self, data):
         new_node = Node(data)

         if self.head is None: # 링크드 리스트 비어 있어 있을 때
            self.head = new_node
            self.tail = new_node
         else: # 비어있지 않을떄
            self.tail.next = new_node
            self.tail = new_node

    def __str__(self):
        temp = '|'
        iterator = self.head
        while(iterator is not None):
            temp += " {} | ".format(iterator.data)
            iterator = iterator.next
        
        return temp
            
l_list = LinkedList()
l_list.append(2)
l_list.append(3)
l_list.append(4)

node = l_list.find_node_at(21)
print(l_list)
l_list.insert_after(node, 111)
print(l_list)


