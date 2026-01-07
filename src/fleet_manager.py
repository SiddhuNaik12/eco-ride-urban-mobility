class FleetManager:
    def __init__(self):
        self.hubs = {}
    def add_hub(self, hub_name: str) -> None:
        if hub_name in self.hubs:
            print("Hub already exists")
        else:
            self.hubs[hub_name] = []
            print(f"Hub '{hub_name}' added")
    def add_vehicle_to_hub(self, hub_name: str, vehicle) -> None:
        if hub_name not in self.hubs:
            print("Hub not found")
            return
        vehicles = self.hubs[hub_name]
        # duplicate check using list comprehension
        if any(v == vehicle for v in vehicles):
            print("Duplicate vehicle ID not allowed")
            return
        vehicles.append(vehicle)
        print(f"Vehicle added to {hub_name}")
    
    def search_by_hub(self, hub_name: str) -> None:
        if hub_name not in self.hubs:
            print("Hub not found")
            return
        vehicles = self.hubs[hub_name]
        if not vehicles:
            print("No vehicles in this hub")
            return
        print(f"\nVehicles in hub: {hub_name}")
        for v in vehicles:
            print(" ", v)
    def search_by_battery(self, min_battery: float) -> None:
        print(f"\nVehicles with battery > {min_battery}%")
        found = False
        for hub, vehicles in self.hubs.items():
            # using filter + lambda
            high_battery = list(filter(lambda v: v.get_battery() > min_battery, vehicles))
            for v in high_battery:
                print(f"Hub: {hub} -> {v}")
                found = True
        if not found:
            print("No vehicles found")
    def show_fleet(self) -> None:
        for hub, vehicles in self.hubs.items():
            print(f"\nHub: {hub}")
            if not vehicles:
                print("  No vehicles")
            for v in vehicles:
                print(" ", v)
    def view_by_vehicle_type(self) -> None:
        # dictionary to group vehicles by type
        categorized = {"Car": [],"Scooter": [] }
        # go through all hubs and their vehicles
        for vehicles in self.hubs.values():
            for v in vehicles:
                # check vehicle type and group accordingly
                if v.__class__.__name__ == "ElectricCar":
                    categorized["Car"].append(v)
                elif v.__class__.__name__ == "ElectricScooter":
                    categorized["Scooter"].append(v)
        # display cars
        print("\nCars:")
        if not categorized["Car"]:
            print("  No cars available")
        else:
            for car in categorized["Car"]:
                print(" ", car)

        # display scooters
        print("\nScooters:")
        if not categorized["Scooter"]:
            print("  No scooters available")
        else:
            for scooter in categorized["Scooter"]:
                print(" ", scooter)
    def fleet_analytics(self) -> None:
        # dictionary to store count of each status
        status_count = {
            "Available": 0,
            "On Trip": 0,
            "Under Maintenance": 0
        }
        # go through all hubs and vehicles
        for vehicles in self.hubs.values():
            for v in vehicles:
                status = v.get_status()
                if status in status_count:
                    status_count[status] += 1
        # display summary
        print("\nFleet Analytics Summary")
        print("-----------------------")
        for status, count in status_count.items():
            print(f"{status}: {count}")
    def sort_vehicles_in_hub(self,hub_name:str)->None:
        if hub_name not in self.hubs:
            print("Hub not found")
            return
        vehicles=self.hubs[hub_name]
        
        if not vehicles:
            print("No vehicles in this hub to sort")
            return
        vehicles.sort(key=lambda v:v.model)
        print(f"\nVehicles in '{hub_name}' sorted by model name:")
        for v in vehicles:
            print(" ",v)
    
