from linked_list import ListNode, SingleLinkedList

class Queue:
  def __init__(self):
    # initialize a linked list to store item

    self.linked_list = SingleLinkedList()
    return

  def enqueue(self, item):
    # put the item to the tail of queue

    self.linked_list.add_list_item(item)
    return

  def dequeue(self):
    # to return the first item of the queue and remove it

    if self.linked_list.head is not None:
      current_node = self.linked_list.head
      self.linked_list.head =  self.linked_list.head.next   
      return current_node.data

  def empty(self):
    # to clear all the items in the queue

    self.linked_list.head = None
    return


  def size(self):
    # to return the length of the queue

    size = 0
    current_node = self.linked_list.head

    while current_node is not None:
      size = size + 1
      current_node = current_node.next
    
    return size

  def output_list(self):
    # outputs the queue (the value of the node, actually)

    self.linked_list.output_list()
    return




"""
queue = Queue()
queue.dequeue()
queue.enqueue(2)
queue.enqueue(5)
queue.enqueue(3)
print(queue.dequeue())
print(queue.size())
queue.output_list()
"""