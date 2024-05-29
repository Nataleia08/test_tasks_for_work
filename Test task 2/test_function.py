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



if __name__ == '__main__':
    unittest.main()

