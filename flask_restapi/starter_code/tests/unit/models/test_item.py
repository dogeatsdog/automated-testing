from unittest import TestCase

from models.item import ItemModel

class ItemTest(TestCase):
    def test_create_item(self):
        item = ItemModel('test', 19.99)

        self.assertEqual(item.name, 'test', 'Error')
        self.assertEqual(item.price, 19.99, 'Error')

    def test _item_json(self):
        item = ItemModel('test', 19.99)

        expected = {
            'name':'test',
            'price':19.99
        }

        self.assertEqual(item.json(), expected)