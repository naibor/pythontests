import unittest

from app.phonebook import Contact 

class TestPhonebook(unittest.TestCase):
	"""docstring for testContact"""

	def test_add_method_adds_contact(self):
		bens_phonebook = Contact()
		bens_phonebook.add("naibor","0707981133")
		self.assertEqual(bens_phonebook.contact_list[0]['naibor'],"0707981133" )

	def test_delete_method_deletes_duplicates(self):
		naibor_phonebook = Contact()
		naibor_phonebook.delete("naibor","0707981133")
		self.assertNotIn(naibor_phonebook.contact_list )



# if __name__ == '__main__':
# 	unittest.main()
# 	def test_add_method_is_a dict():
# 		self.

# 	def test_add_method_value_is_an_integer():
# 		self.

# # asserts its a dict
# # asserts value is an integer


# 	def test_phonebook_update_method_return_correct_result(self):

# 	def test_phonebook_delete method_return_correct_result(self):

# 	def test_phonebook_view_method_return_correct_result(self):
		


