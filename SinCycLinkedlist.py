class Node(object):
	def __init__(self,item):
		self.item=item
		self.next=None

class SinCycLinkedlist(object):
	def __init__(self):
		self._head=None

	def is_empty(self):
		return self._head==None

	def length(self):
		if self.is_empty():
			return 0
		count=1
		cur=self._head
		while cur.next!=self._head:
			count+=1
			cur=cur.next

		return count

	def travel(self):
		if self.is_empty():
			return
		cur=self._head
		print(cur.item)
		while cur.next !=self._head:
			cur=cur.next
			print(cur.item,)
		print("")

	def add(self,item):
		node=Node(item)
		if self.is_empty():
			self._head=node
			node.next=self._head
		else:
			node.next=self._head
			cur=self._head
			while cur.next!=self._head:
				cur=cur.next
			cur.next=node

			self._head=node

	def append(self,item):
		node=Node(item)
		if self.is_empty():
			self._head=node
			node.next=self._head

		else:
			cur=self._head
			while cur.next !=self._head:
				cur=cur.next
			cur.next=node
			node.next=self._head


	def insert(self,pos,item):
		if pos<=0:
			self.add(item)
		elif pos>(self.length()-1):
			self.append(item)
		else:
			node=Node(item)
			cur=self._head
			count=0

			while count<(pos-1):
				count+=1
				cur=cur.next
			node.next=cur.next
			cur.next=node

	def remove(self,item):
		if self.is_empty():
			return
		cur=self._head
		pre=None

		if cur.item==item:
			if cur.next!=self._head:
				while cur.next!=self._head:
					cur=cur.next
				cur.next=self._head.next
				self._head=self._head.next
			else:
				self._head=None
		else:
			pre=self._head

			while cur.next!=self._head:
				if cur.item==item:
					pre.next=cur.next
					return
				else:
					pre=cur
					cur=cur.next

			if cur.item==item:
				pre.next=cur.next
	def search(self,item):
		if self.is_empty():
			return False
		cur=self._head
		if cur.item==item:
			return True
		while cur.next !=self._head:
			cur=cur.next
			if cur.item==item:
				return True
		return False

if __name__=="__main__":
	ll=SinCycLinkedlist()
	ll.add(1)
	ll.add(2)
	ll.append(3)
	ll.insert(2,4)
	ll.insert(4,5)
	ll.insert(0,6)
	print("length:",ll.length())
	ll.travel()
	print(ll.search(3))
	print(ll.search(7))
	ll.remove(1)
	print("length:",ll.length())
	ll.travel()