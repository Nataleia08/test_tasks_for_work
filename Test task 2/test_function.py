import unittest
from function import SolarPanel, WindTurbine, HydroPlant

class TestEnergySource(unittest.TestCase):
    def test_1(self):
        energy_source1 = SolarPanel()
        result1 = energy_source1.AnnualEnergyOutput([20, 15])
        self.assertEqual(result1, 4500.0)
    
    def test_2(self):
        energy_source2 = WindTurbine()
        result1 = energy_source2.AnnualEnergyOutput([50, 6])
        self.assertEqual(result1, 45000.0)

    def test_3(self):
        energy_source3 = HydroPlant()
        result1 = energy_source3.AnnualEnergyOutput([300, 20])
        self.assertEqual(result1, 72000.0)

class TestResourceDepletionRate(unittest.TestCase):
    def test_4(self):
        energy_source_4 = SolarPanel()
        result4 = energy_source_4.ResourceDepletionRate([20, 15])
        self.assertEqual(result4, 6.67)

    def test_5(self):
        energy_source_5 = WindTurbine()
        result5 = energy_source_5.ResourceDepletionRate([50, 6])
        self.assertEqual(result5, 3.33)

    def test_6(self):
        energy_source_6 = HydroPlant()
        result6 = energy_source_6.ResourceDepletionRate([300, 20])
        self.assertEqual(result6, 15.00)

if __name__ == '__main__':
    unittest.main()

