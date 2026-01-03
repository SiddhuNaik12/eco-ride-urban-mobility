from vehicle import Vehicle
def main() -> None:
    print("Welcome to Eco-Ride Urban Mobility System")
    vehicle_1 = Vehicle("EV101", "Ather 450X", 85.5, "Good", 120.0)
    print(vehicle_1)
    vehicle_1.set_battery_percentage(90)
    vehicle_1.set_maintenance_status("Needs Service")
    print("\nAfter Update:")
    print(vehicle_1)
if __name__ == "__main__":
    main()
