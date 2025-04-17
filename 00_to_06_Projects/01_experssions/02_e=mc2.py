 # Einstein's famous equation E=mc^2
    # E = mc^2
    # where:
    # E = energy (in joules)
    # m = mass (in kilograms)
    # c = speed of light (in meters per second)

C: int = 299792458  # The speed of light in m/s
def main():
    mass_in_kg: float = float(input("\033[1m\033[3mEnter mass in Kg:\033[0m "))
    # Calculate energy
    # equivalently energy = mass * (C ** 2)
    # using the ** operator to raise C to the power of 2
    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Display work to the user
    print("e = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    
    print("E = " + str(energy_in_joules) + " Joules of energy")

if __name__ == '__main__':
    main()