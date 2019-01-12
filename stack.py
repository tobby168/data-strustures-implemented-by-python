class Stack:
  def __init__(self, data = None):
    # create a list that store data

    if data == None:
      self.stack = list()
    elif isinstance(data, list):
      self.stack = data
    else:
      raise ValueError('input data should be list')
    return

  def push(self, data):
    # put data into the top of stack

    self.stack.append(data)
    return

  def pop(self):
    # remove the data on the top and return it

    return self.stack.pop()

  def output_stack(self):
    # print the full stack
    
    data = []
    for x in self.stack:
      data.append(x)

    print(data)
    return

stack1 = Stack()
stack1.push(1)
stack1.push(3)
stack1.push(2)
print(stack1.pop())
stack1.output_stack()

stack2 = Stack([4,6,2,1,6,3])
stack2.pop()
stack2.output_stack()