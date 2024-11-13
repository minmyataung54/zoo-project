import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.

    def test_crawler_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), "Not available age")

    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(18), 100)

    def test_senior_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(70), 100)

    def test_middle_age_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(40), 150)

if __name__ == '__main__':
    unittest.main()