class EnergySource:
    def __init__(self, type:str) -> None:
        self.type = type

    def AnnualEnergyOutput(self, *args) -> float:
        result = 1
        for arg in args[0]:
            result = result*arg
        return result
    
    def ResourceDepletionRate(self, *args) -> float:
        return 1/self.AnnualEnergyOutput(args)
    

class SolarPanel(EnergySource):
    def __init__(self) -> None:
        super().__init__("SolarPanel")
        self.par = 15
        self.coef = 100

    def AnnualEnergyOutput(self, *args) -> float:
        return self.par*super().AnnualEnergyOutput(*args)
    
    def ResourceDepletionRate(self, *args) -> float:
        return round(self.coef/args[0][-1], 2)


class  WindTurbine(EnergySource):
    def __init__(self) -> None:
        super().__init__("WindTurbine")
        self.par = 150
        self.coef = 1000

    def AnnualEnergyOutput(self, *args) -> float:
        return self.par*super().AnnualEnergyOutput(*args)
    
    def ResourceDepletionRate(self, *args) -> float:
        return round(self.coef/super().AnnualEnergyOutput(*args), 2)


class HydroPlant(EnergySource):
    def __init__(self) -> None:
        super().__init__("HydroPlant")
        self.par = 12

    def AnnualEnergyOutput(self, *args) -> float:
        return self.par*super().AnnualEnergyOutput(*args)
    
    def ResourceDepletionRate(self, *args) -> float:
        return round(args[0][0]/args[0][1], 2)