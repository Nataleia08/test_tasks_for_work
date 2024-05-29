from function import SolarPanel, WindTurbine, HydroPlant

def main():
    while True:  
        user_input = input("\nEnter command >>> ")
        if not user_input:
            print("\nGood bay!")
            break
        try:
            sample_input = user_input.split(" ")
            parameters = list(map(float, sample_input[2::2]))
            match sample_input[0]:
                case "SolarPanel": new_energy_source = SolarPanel()
                case "WindTurbine": new_energy_source = WindTurbine()
                case "HydroPlant": new_energy_source = HydroPlant()
            energy_output = new_energy_source.AnnualEnergyOutput(parameters)
            if energy_output == 1:
                print("This is not energy source")
            else: 
                print(f"{new_energy_source.type} AnnualEnergyOutput {energy_output}")
        except TypeError as e:
            print(f"This command not right! {e}")

        
if __name__ == "__main__":
    main()