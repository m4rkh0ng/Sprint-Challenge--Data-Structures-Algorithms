class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    current = self.value
    if current is None:
      return
    # start by adding current/root value to arr by calling cb
    cb(current)
    # traverse left sides and then right sides by calling itself recursively  
    if self.left != None:
      self.left.depth_first_for_each(cb)
    if self.right != None:
      self.right.depth_first_for_each(cb)

  def breadth_first_for_each(self, cb):
    nodes = []
    nodes.append(self)

    while len(nodes) > 0:
      # remove and return root/value
      node = nodes.pop(0)
      # append that value to the arr by calling cb with that value as x 
      cb(node.value)
      #checking left or right, if they exist, add them onto nodes
      if node.left != None:
        nodes.append(node.left)
      if node.right != None:
        nodes.append(node.right)

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
