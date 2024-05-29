class EnergySource:
    def __init__(self, type:str) -> None:
        self.type = type

    def AnnualEnergyOutput(self, *args) -> float:
        result = 1
        for arg in args[0]:
            result = result*arg
        return result
    
    def Calculations(self, command) -> float:
        try:
            par_list = command.split(" ")
            parameters = list(map(float, par_list[2::2])) 
            match self.type:
                case "SolarPanel": parameters.append(15)
                case "WindTurbine": parameters.append(150)
                case "HydroPlant": parameters.append(12)
                case "OffshoreWindTurbine": 
                    parameters[-1] = 1 - parameters[-1]
                    parameters.append(160)
            energy_output = self.AnnualEnergyOutput(parameters)
            if energy_output == 1:
                print("This is not energy source")
            else: 
                print(f"{self.type} AnnualEnergyOutput {energy_output}")
                return energy_output
        except TypeError as e:
            print(f"This command not right! {e}")
