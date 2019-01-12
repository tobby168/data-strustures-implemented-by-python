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