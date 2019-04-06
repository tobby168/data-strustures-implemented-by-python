import hashlib
import string
import random
import time

class BloomFilter:

  # to initialize bloom filter with customed array size and hash functions.
  def __init__(self, size = 1000, hash = 3):
    self.size = size
    self.array = [False] * size
    self.hashs = [hashlib.md5, hashlib.sha1, hashlib.sha224, hashlib.sha256, hashlib.sha384]
    if hash > 5:
      print('Amount of hash functions should be less than 5. Set to 5.')
    else:
      self.hashs = self.hashs[:hash]
    return

  # to convert data with hash functions and set the filter.
  def add_data(self, data):
    data = data.encode('utf-8')
    for hash_func in self.hashs:
      idx = int(hash_func(data).hexdigest(), 16) % self.size
      self.array[idx] = True
    return

  # to check if data can pass the filter. 
  def is_exist(self, data):
    data = data.encode('utf-8')
    for hash_func in self.hashs:
      idx = int(hash_func(data).hexdigest(), 16) % self.size
      if not self.array[idx]:
        return False
    return True

  # to test the fail negative rate of the filter.
  def test(self):
    start_time = time.time()
    true = len([bit for bit in self.array if bit])
    print('There are {} True in the {} bit.'.format(true, self.size))
    print('With {} hash functions, calculated false negative rate is {:2.5f}%.'.format(len(self.hashs), (true / self.size) ** len(self.hashs) * 100))

    fail, tests = 0, 1000000
    for _ in range(tests):
      if bloom.is_exist(randomString(random.randint(5,15))):
        fail += 1
    print('In {} test cases, the false negative rate is {:2.5f}%.'.format(tests, fail / tests * 100))
    print('This test takes {:.2f}s'.format(time.time()-start_time))

# to randomly generate string in lowercase
def randomString(length):
      letters = string.ascii_lowercase
      return ''.join(random.choice(letters) for i in range(length))

bloom = BloomFilter()
texts = []
for _ in range(100):
  text = randomString(random.randint(5,15))
  texts.append(text)
  bloom.add_data(text)
print(bloom.is_exist(texts[0]))
print(bloom.is_exist(randomString(10)))
bloom.test()


