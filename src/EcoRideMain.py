from fleet_manager import FleetManager
from vehicle import ElectricCar, ElectricScooter
def main() -> None:
    print("Welcome to Eco Ride Urban Mobility System")
    manager = FleetManager()
    # Load CSV or JSON data if exists
    manager.load_from_csv()
    manager.load_from_json()
    while True:
        print("\n1. Add Hub")
        print("2. Add Vehicle to Hub")
        print("3. View Fleet")
        print("4. Exit")
        print("5. Search vehicles by hub")
        print("6. Search vehicles with battery > 80")
        print("7. View vehicles by type")
        print("8. Fleet analytics")
        print("9. Sort vehicles in a hub alphabetically")
        print("10. Sort vehicles by battery level")
        print("11. Sort vehicles by fare price")
        print("12. Save fleet to CSV")
        print("13. Save fleet to JSON")
        choice = input("Enter choice: ")
        if choice == "1":
            hub = input("Enter hub name: ")
            manager.add_hub(hub)
        elif choice == "2":
            hub = input("Enter hub name: ")
            vtype = input("Car or Scooter: ").lower()
            vid = input("Vehicle ID: ")
            model = input("Model: ")
            battery = float(input("Battery %: "))
            status = input("Status: ")
            price = float(input("Base Price: "))
            if vtype == "car":
                seats = int(input("Seats: "))
                vehicle = ElectricCar(vid, model, battery, status, price, seats)
            else:
                speed = int(input("Max Speed: "))
                vehicle = ElectricScooter(vid, model, battery, status, price, speed)
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
        elif choice == "8":
            manager.fleet_analytics()
        elif choice == "9":
            hub = input("Enter hub name: ")
            manager.sort_vehicles_in_hub(hub)
        elif choice == "10":
            manager.sort_by_battery()
        elif choice == "11":
            manager.sort_by_price()
        elif choice == "12":
            manager.save_to_csv()
        elif choice == "13":
            manager.save_to_json()
        else:
            print("Invalid Option")
if __name__ == "__main__":
    main()
