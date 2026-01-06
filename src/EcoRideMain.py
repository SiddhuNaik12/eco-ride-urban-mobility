from vehicle import ElectricCar, ElectricScooter
from fleet_manager import FleetManager

def main() -> None:
    print("Welcome to Eco Ride Urban Mobility System")
    manager = FleetManager()
    while True:
        print("\n1. Add Hub")
        print("2. Add Vehicle to Hub")
        print("3. View Fleet")
        print("4. Exit")
        print("5. Search vehicles by hub")
        print("6. Search vehicles with battery > 80")
        print("7. View vehicles by type")
        choice = input("Enter choice: ")
        if choice == "1":
            hub = input("Enter hub name: ")
            manager.add_hub(hub)
        elif choice == "2":
            hub = input("Enter hub name: ")
            v_type = input("Car or Scooter: ").lower()
            vid = input("Vehicle ID: ")
            model = input("Model: ")
            battery = float(input("Battery %: "))
            status = input("Status: ")
            price = float(input("Base price: "))
            if v_type == "car":
                seats = int(input("Seats: "))
                vehicle = ElectricCar(vid, model, battery, status, price, seats)
            elif v_type == "scooter":
                speed = int(input("Max speed: "))
                vehicle = ElectricScooter(vid, model, battery, status, price, speed)
            else:
                print("Invalid vehicle type")
                continue
            manager.add_vehicle_to_hub(hub, vehicle)
        elif choice == "3":
            manager.show_fleet()
        elif choice == "4":
            print("Exiting system")
            break
        elif choice == "5":
            hub = input("Enter hub name: ")
            manager.search_by_hub(hub)
        elif choice == "6":
            manager.search_by_battery(80)
        elif choice == "7":
            manager.view_by_vehicle_type()

        else:
            print("Invalid option")
if __name__ == "__main__":
    main()
