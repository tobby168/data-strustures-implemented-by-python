class ListNode:
  def __init__(self, data): 
    # initialize this object

    # store data
    self.data = data

    # store the reference (next item)
    self.next = None
    return
  
  def has_value(self, value): 
    # method to compare the value with the node data

    if self.data == value:
      return True
    else:
      return False

node1 = ListNode(15)  
#print(type(node1)) # <class '__main__.ListNode'>


class SingleLinkedList:
  def __init__(self): 
    # initialize this object

    self.head = None
    self.tail = None
    return

  def add_list_item(self, item):
    # make sure item is a proper node

    if not isinstance(item, ListNode):
      item = ListNode(item)
    
    if self.head is None:
      self.head = item
    else:
      self.tail.next = item
    
    self.tail = item
    return
    
  def list_length(self):
    #returns the number of list items

    count = 0
    current_node = self.head

    while current_node is not None:
      count = count + 1

      # jump to the linked node
      current_node = current_node.next 
    return count

  def output_list(self):
    # outputs the list (the value of the node, actually)

    current_node = self.head
    results = []

    while current_node is not None:
      results.append(current_node.data)

      # jump to the linked node
      current_node = current_node.next 

    print(results)
    return

  def unordered_search(self, value):
    # search the linked list for the node that has this value

    # define current_node
    current_node = self.head

    # define position
    node_id = 1

    # define list of results
    results = []

    while current_node is not None:
      if current_node.data == value:
        results.append(node_id)
      
      node_id = node_id + 1
      current_node = current_node.next

    return results

  def remove_list_item_by_id(self, id):
    # remove the list item with the item id

    current_id = 1
    current_node = self.head
    previous_node = None

    while current_node is not None:
      if current_id == id:
        if previous_node is not None:
          previous_node.next = current_node.next
        else:
          self.head = current_node.next
      previous_node = current_node
      current_node = current_node.next
      current_id = current_id + 1
    return

  def reverse(self):
    # reverse the order of the list

    previous_node = None
    current_node = self.head
    next_node = current_node.next

    while next_node is not None:
      current_node.next = previous_node
      previous_node = current_node
      current_node = next_node
      next_node = next_node.next

    current_node.next = previous_node
    self.head = current_node
    return
  
  def remove_value(self, value):
    #remove the first item in the list with this value

    previous_node = None
    current_node = self.head

    while current_node is not None:
      if current_node.data == value:
        previous_node.next = current_node.next
        return

      previous_node = current_node
      current_node = current_node.next

    return



"""
list1 = SingleLinkedList()
list1.add_list_item(node1)
list1.add_list_item('12')
list1.add_list_item(15)
list1.add_list_item(17)
list1.remove_list_item_by_id(3)
list1.reverse()
list1.remove_value(15)
list1.output_list()
"""