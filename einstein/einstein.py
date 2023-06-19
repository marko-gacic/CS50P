def main():
    mass = int(input("m: "))
    energy = calculate_energy(mass)
    print("E:", energy)

def calculate_energy(mass):
    speed = 300000000
    energy = mass * speed ** 2
    return energy
if __name__ == "__main__":
    main()