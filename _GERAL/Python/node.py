from cgi import test


class Node:
  def __init__(self, value: int) -> None:
    self.value: int = value
    self.left: Node = None
    self.right: Node = None
    
def insert(node: Node, value: int) -> Node:
  if node == None:
    return Node(value)
  if value < node.value:
    node.left = insert(node.left, value)
  else:
    node.right = insert(node.right, value)
  return node


def order(node: Node):
  if node == None:
    return
  order(node.left)
  print(node.value, end = " ")
  order(node.right)
  
  
root: Node = None
values: list[int] = [22, 44, 555, 666, 98, 1, 20]

for value in values:
  root = insert(root, value)

order(root)