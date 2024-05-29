class EnergySource:
    def __init__(self, type:str) -> None:
        self.type = type

    def AnnualEnergyOutput(self, *args) -> float:
        result = 1
        for arg in args[0]:
            result = result*arg
        return result
    

class SolarPanel(EnergySource):
    def __init__(self) -> None:
        super().__init__("SolarPanel")
        self.par = 15

    def AnnualEnergyOutput(self, *args) -> float:
        return self.par*super().AnnualEnergyOutput(*args)


class  WindTurbine(EnergySource):
    def __init__(self) -> None:
        super().__init__("WindTurbine")
        self.par = 150

    def AnnualEnergyOutput(self, *args) -> float:
        return self.par*super().AnnualEnergyOutput(*args)


class HydroPlant(EnergySource):
    def __init__(self) -> None:
        super().__init__("HydroPlant")
        self.par = 12

    def AnnualEnergyOutput(self, *args) -> float:
        return self.par*super().AnnualEnergyOutput(*args)