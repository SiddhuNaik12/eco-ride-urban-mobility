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
    def show_fleet(self) -> None:
        for hub, vehicles in self.hubs.items():
            print(f"\nHub: {hub}")
            if not vehicles:
                print("  No vehicles")
            for v in vehicles:
                print(" ", v)
