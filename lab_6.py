from lab06001 import Node
class LinkedList(): #create the attributs
	def __init__(self, head = None , size = 0, tail=None):
		self.head = head
		self.size = size 
		self.tail = tail
	# create the getters and the setters
	def set_head (self,h):
		self.head = h
	def get_head(self,head):
		return(self.head)

	def set_size(self,s):
		self.size = s 
	def get_size(self,size):
		return(self.size)

	def set_tail(self,t):
		self.tail = t
	def get_tail(self,tail):
		return(self.tail )
	#create the two methods 
	def isEmpty(self):
		if(self.get_size() > 0):
			return(False)
		else:
			return(True)
	def addnode(self,n):
		NewNode = Node(data = n)
		#add the new head or show it, and check if it is empty
		if (self.isEmpty()):
			self.set_head(NewNode)
		else:
		
			self.get_tail().set_nextPointer(NewNode) 
		
		self.set_tail(NewNode)
		self.set_size(size + 1)

def main():
	pass
if __name__ == '__main__':
		main()
		
	