class Contact (object):
	"""docstring foContact """
	def __init__(self):
		self.contact_list=[]
# class variable
	def add(self,name,number):
		self.newcontact={}
		self.newcontact[name]=number
		self.contact_list.append(self.newcontact)
		return self.newcontact

	def view():
		self.contact_list

		pass

	def delete(self,name ):
		if name in self.contact_list:
			del self.contact_list[name]
			return self.contact_list()



	




