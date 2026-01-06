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
