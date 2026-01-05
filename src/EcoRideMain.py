from vehicle import ElectricCar, ElectricScooter
def main() -> None:
    print("Welcome to Eco Ride Urban Mobility System")
    car = ElectricCar("EC301","Tata Nexon EV",90.0,"Good",15.0,5)
    scooter = ElectricScooter("ES401","Ola S1",80.0,"Good",10.0,90)
    distance = 10.0
    print("\nCar Details")
    print(car)
    print("Trip Cost:", car.calculate_trip_cost(distance))
    print("\nScooter Details")
    print(scooter)
    print("Trip Cost:", scooter.calculate_trip_cost(distance))
if __name__ == "__main__":
    main()
