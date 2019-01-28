class maxPQ:
  # implement a maximum priority queue by binary heap
  def __init__(self):
    self.pq = list([None]) # pq stands for priority queue
    self.length = 0
    return

  def isEmpty(self):
    return self.length == 0

  def insert(self, item):
    # insert item to the end then swim it up
    self.pq.append(item)
    self.length = self.length + 1
    self.__swim(self.length)
    return

  def delMax(self):
    # exchange first item and last item, then order again
    maximum = self.pq[1]
    self.__exchange(1, self.length),
    self.pq.pop()
    self.length = self.length - 1
    self.__sink(1)
    
    return maximum

  def __swim(self, k):
    # Exchange key in child with key in parent. Repeat until heap order restored.
    while k > 1 and self.__less(k // 2, k):
      self.__exchange(k // 2, k)
      k = k // 2
    return

  def __sink(self, k):
    # Key in parent exchange with ket in larger child. Repeat until heap order restored.
    while k * 2 <= self.length:
      j = k * 2
      if j < self.length and self.__less(j, j + 1):
        j = j + 1

      self.__exchange(k, j + 1)
      k = j
      

  def __less(self, a, b):
    # return a boolean represent if item at a position is less than item at b
    if self.pq[a] < self.pq[b]:
      return True
    else:
      return False
  
  def __exchange(self, a, b):
    # swap item in the heap at position a and b
    temp = self.pq[a]
    self.pq[a] = self.pq[b]
    self.pq[b] = temp
    return

"""
pq = maxPQ()
pq.insert(2)
pq.insert(3)
pq.insert(5)
pq.insert(8)
print(pq.delMax())
print(pq.pq)
"""