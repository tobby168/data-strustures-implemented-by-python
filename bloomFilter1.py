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
