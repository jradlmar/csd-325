# Jared Morris
# Module 7 Assignment

import unittest
from city_functions import city_country


class CitiesTestCase(unittest.TestCase):
    """Tests for city_functions.py."""

    def test_city_country(self):
        """Does Santiago, Chile work correctly?"""
        formatted_city = city_country("Santiago", "Chile")
        self.assertEqual(formatted_city, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()