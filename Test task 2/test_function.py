import unittest
from function import EnergySource

class TestEnergySource(unittest.TestCase):
    def test_1(self):
        energy_source1 = EnergySource("SolarPanel")
        result1 = energy_source1.Calculations("SolarPanel Area 20 Efficiency 15")
        self.assertEqual(result1, 4500.0)
    
    def test_2(self):
        energy_source2 = EnergySource("WindTurbine")
        result1 = energy_source2.Calculations("WindTurbine Height 50 WindSpeedAverage 6")
        self.assertEqual(result1, 45000.0)

    def test_3(self):
        energy_source3 = EnergySource("HydroPlant")
        result1 = energy_source3.Calculations("HydroPlant FlowRate 300 Drop 20")
        self.assertEqual(result1, 72000.0)



if __name__ == '__main__':
    unittest.main()

