#city_functions.py

def city_country(city, country):
    """Return a string like 'City, Country'."""
    return f"{city.title()}, {country.title()}"

#test_cities.py

import unittest
from city_functions import city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Does a simple city and country work?"""
        formatted_name = city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()
