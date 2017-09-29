import unittest
from city_function import get_city_function

class CityTestCase(unittest.TestCase):
	"""用于测试输入的城市与国家的名字是否正确？"""
	def test_city_county(self):
		full_name = get_city_function('santiago', 'chile')
		self.assertEqual(full_name, 'Santiago, Chile')
		
	"""用于测试加上人口数量的情况是否正确？"""
	def test_city_country_population(self):
		full_name = get_city_function('santiago', 'chile', '20000')
		self.assertEqual(full_name, 'Santiago, Chile - Population 20000')
		
unittest.main()