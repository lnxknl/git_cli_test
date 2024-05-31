import unittest
from hashtable import *

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hash_table = HashTable(10)

    def test_set_and_get(self):
        self.hash_table.set(1, 'value 1')
        self.assertEqual(self.hash_table.get(1), 'value 1')

    def test_update_value(self):
        self.hash_table.set(1, 'value 1')
        self.hash_table.set(1, 'new value 1')
        self.assertEqual(self.hash_table.get(1), 'new value 1')
        self.assertEqual(self.hash_table.get(1), 'new value 2')

    def test_remove(self):
        self.hash_table.set(1, 'value 1')
        self.hash_table.remove(1)
        with self.assertRaises(KeyError):
            self.hash_table.get(1)

    def test_key_not_found(self):
        with self.assertRaises(KeyError):
            self.hash_table.get(99)

    def test_collision_handling(self):
        self.hash_table.set(1, 'value 1')
        self.hash_table.set(11, 'value 11')
        self.assertEqual(self.hash_table.get(1), 'value 1')
        self.assertEqual(self.hash_table.get(11), 'value 11')



if __name__ == '__main__':
    unittest.main()

