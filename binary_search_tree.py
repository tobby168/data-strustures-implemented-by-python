class BST:

  # to initialize a BST, construct a node to be the root
  def __init__(self):
    self.root = None
    return

  # to create a new key-value pair
  # or to update a existed key-value pair
  def put(self, key, value):
    self.root = self.__putNode(self.root, key, value)
    return

  def __iter__(self):
    queue = list()
    self.__inorder(self.root, queue)
    return iter(queue)

  def __inorder(self, node, queue):
    if node is None:
      return 
    self.__inorder(node.left, queue)
    queue.append(node.key)
    self.__inorder(node.right, queue)

  # put a node in order
  def __putNode(self, node, key, value):
    # if there is not a node, then create a new one
    if node == None:
      return self.__node(key, value)

    compare = self.__compateTo(key, node.key)
    # if the new key is smaller than current node, shift to the left
    if compare < 0:
      node.left = self.__putNode(node.left, key, value)
    # if the new key is larger than current node, shift to the left
    elif compare > 0:
      node.right = self.__putNode(node.right, key, value)
    # if the new key is equal to current node, update the value
    else:
      node.value = value

    # update the node
    # count of nodes in this tree is the sum of 2 subtree's size and itself
    node.count = 1 + self.__sizeNode(node.left) + self.__sizeNode(node.right)
    return node

  # to get the value of given key
  def get(self, key):
    node = self.root
    while node is not None:
      compare = self.__compateTo(key, node.key)
      if compare < 0:
        node = node.left
      elif compare > 0:
        node = node.right
      else:
        return node.value
    
    return None

  # return the number of nodes in the tree
  def size(self):
    return self.__sizeNode(self.root)

  # return the number of nodes in the subtree with the root of this node
  @staticmethod
  def __sizeNode(node):
    if node is None:
      return 0
    else:
      return node.count

  # return how many keys are smaller than a specific key 
  def rank(self, key):
    return self.__rankNode(self.root, key)

  # return how many keys are smaller than a specific key in the subtree with the root of this node
  def __rankNode(self, node, key):
    if node is None:
      return 0
    
    compare = self.__compateTo(key, node.key)
    # if the specific key is smaller than the node's key, shift to the left subtree.
    if compare < 0:
      return self.__rankNode(node.left, key)
    # if the specific key is larger than the node's key, add the node itself and all the nodes in the left subtree.
    # than shift to the right subtree
    elif compare > 0:
      return 1 + self.__sizeNode(node.left) + self.__rankNode(node.right, key)
    else:
      return self.__sizeNode(node.left)

  # every node has 5 fields: key, value, reference to left subtree, reference to right subtree, count of nodes in subtrees
  class __node:
    def __init__(self, key = None, value = None):
      self.key = key
      self.value = value
      self.left = None
      self.right = None
      self.count = 1
      return

  @staticmethod
  def __compateTo(a, b):
    if a > b:
      return 1
    elif a < b:
      return -1
    else:
      return 0
      
BST = BST()
BST.put('d', 20)
BST.put('a', 15)
BST.put('d', 12)
BST.put('f', 22)
BST.put('c', 18)
print(BST.get('d'))
print(BST.size())
print(BST.rank('e'))

for key in BST:
  print(key, end = ' ')
print('\n')