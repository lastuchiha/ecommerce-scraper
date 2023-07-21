import unittest
from flipkart import Flipkart


class FlipkartTest(unittest.TestCase):
    def setUp(self):
        with open('urls.txt', 'r') as f:
            self.urls = f.readlines()

    def test_available_product_1(self):
        product_details = Flipkart(self.urls[0]).get_details(additional=True)

        self.assertEqual(product_details, {
            'id': 'itm6e30c6ee045d2',
            'price': '₹60,999',
            'title': 'APPLE iPhone 13 (Pink, 128 GB)',
            'mrp': '₹69,900',
            'rating': '4.7'
        })

    def test_available_product_2(self):
        product_details = Flipkart(self.urls[1]).get_details()

        self.assertEqual(product_details, {
            'id': 'itm49862bfa6db55',
            'title': 'PLAYSKOOL Marvel Super Hero Adventures Mega Mighties Black Panther, 10-Inch Action Figure(Multicolor)',
            'price': '₹849',
            'mrp': '₹999'
        })

    def test_not_available_product_1(self):
        product_details = Flipkart(self.urls[2]).get_details()

        self.assertEqual(product_details, {
            'id': 'itm769579d720c14',
            'title': 'VANSSneakers For Men(Black)',
            'price': '₹3,999',
            'mrp': 'N/A'
        })


if __name__ == '__main__':
    unittest.main()
