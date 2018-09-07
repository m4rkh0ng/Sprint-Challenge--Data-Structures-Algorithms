def heapsort(arr):
  #arr to become heap
  #heap then to be sorted
  
  heapify = Heap()
  new_arr = []

  for item in arr:
    heapify.insert(item)
  while len(heapify.storage) > 0:
    new_arr.insert(0, heapify.delete())
  return new_arr


  # def swap(arr, i, j):
  #   temp = arr[i]
  #   arr[i] = arr[j]
  #   arr[j] = temp

  # def siftdown(arr, i, size):
  #   l = 2*i+1
  #   r = 2*i+2
  #   largest = i
  #   if l <= size-1 and arr[l] > arr[i]:
  #     largest = l
  #   if r <= size-1 and arr[r] > arr[largest]:
  #     largest = r
  #   if largest != i:
  #     swap(arr, i, largest)
  #     siftdown(arr, largest, size)

  # def heapify(arr, size):
  #   p = (size//2)-1
  #   while p>=0:
  #     siftdown(arr, p, size)
  #     p -= 1

  # size = len(arr)
  # heapify(arr, size)
  # end = size-1
  # while(end > 0):
  #   swap(arr, 0, end)
  #   siftdown(arr, 0, end)
  #   end -= 1

class Heap:
  def __init__(self):
    self.storage = []
    
  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    retval = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()
    self._sift_down(0)
    return retval 

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      index = (index - 1) // 2

  def _sift_down(self, index):
    while index * 2 + 1 <= len(self.storage) - 1:
      mc = self._max_child(index)
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc

  def _max_child(self, index):
    if index * 2 + 2 > len(self.storage) - 1:
      return index * 2 + 1
    else:
      return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2