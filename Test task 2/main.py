from function import EnergySource

def main():
    while True:  
        user_input = input("\nEnter command >>> ")
        if not user_input:
            print("\nGood bay!")
            break
        try:
            sample_input = user_input.split(" ")
            new_energy_source = EnergySource(sample_input[0])
            new_energy_source.Calculations(user_input)
        except TypeError as e:
                print(f"This command not right! {e}")
        
if __name__ == "__main__":
    main()