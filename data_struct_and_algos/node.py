class Node:
	def __init__(self, value):
		self._value = value
		self._children = []

	def __repr__(self):
		return 'Node({!r})'.format(self._value)

	def add_child(self, node):
		self._children.append(node)

	def __iter__(self):
		return iter(self._children)

	def depth_first(self):
		yield self
		for child in self:
			yield from child.depth_first()


if __name__ == '__main__':
	root = Node(0)
	for x in range(1, 6):
		root.add_child(Node(x))

	for node in root.depth_first():
		print(node)
