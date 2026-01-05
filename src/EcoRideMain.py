from vehicle import ElectricCar, ElectricScooter
def main() -> None:
    print("Welcome to Eco Ride Urban Mobility System")
    # mixed list of vehicles
    vehicles = [
        ElectricCar("EC501", "Tata Nexon EV", 90.0, "Good", 0.0, 5),
        ElectricScooter("ES601", "Ola S1", 80.0, "Good", 0.0, 90)
    ]
    print("\nTrip Cost Calculation")
    for v in vehicles:
        # same method call, different behavior
        cost = v.calculate_trip_cost(10)
        print(f"{v.model} -> Trip Cost: {cost}")
if __name__ == "__main__":
    main()
