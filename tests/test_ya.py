import unittest
from Ya import create_folder, delete_folder

class TestCreateTable(unittest.TestCase):

    def setUp(self):
        self.token = 's'
        self.path = 's'
    
    def test_error_409(self):
        self.assertNotEqual(create_folder(self.path, self.token).status_code, 409)
    
    def test_all_error(self):
        list_erorr = [401, 404, 403, 406, 400, 413, 423, 429, 503, 507]
        for i in list_erorr:
          self.assertNotEqual(create_folder(self.path, self.token).status_code, i)  

    def test_create_folder(self):
        result = create_folder(self.path, self.token)
        self.assertEqual(result.status_code, 201)

    def tearDown(self):
        self.dell = delete_folder(self.path, self.token)