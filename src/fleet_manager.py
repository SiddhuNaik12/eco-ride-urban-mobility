import csv
import json
from vehicle import ElectricCar, ElectricScooter
class FleetManager:
    def __init__(self):
        self.hubs = {}
    # ---------- UC-6: Add Hubs & Vehicles -----------------
    def add_hub(self, hub_name: str) -> None:
        if hub_name not in self.hubs:
            self.hubs[hub_name] = []
            print(f"Hub '{hub_name}' added")
        else:
            print("Hub already exists")
    def add_vehicle_to_hub(self, hub_name: str, vehicle) -> None:
        if hub_name not in self.hubs:
            print("Hub not found")
            return
        vehicles = self.hubs[hub_name]
        # UC-7: duplicate check
        if any(v == vehicle for v in vehicles):
            print("Duplicate vehicle ID not allowed")
            return
        vehicles.append(vehicle)
        print(f"Vehicle added to {hub_name}")
    # ---------- UC-6: View Fleet -----------------
    def show_fleet(self):
        for hub, vehicles in self.hubs.items():
            print(f"\nHub: {hub}")
            if not vehicles:
                print("  No vehicles")
            for v in vehicles:
                print(" ", v)
    # ---------- UC-8: Search -----------------
    def search_by_hub(self, hub_name: str):
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
    def search_by_battery(self, min_battery: float):
        print(f"\nVehicles with battery > {min_battery}%")
        found = False
        for hub, vehicles in self.hubs.items():
            high = list(filter(lambda v: v.get_battery() > min_battery, vehicles))
            for v in high:
                print(f"Hub: {hub} -> {v}")
                found = True
        if not found:
            print("No vehicles found")
    # ---------- UC-9: Categorized View -----------------
    def view_by_vehicle_type(self):
        categorized = {"Car": [], "Scooter": []}
        for vehicles in self.hubs.values():
            for v in vehicles:
                if isinstance(v, ElectricCar):
                    categorized["Car"].append(v)
                else:
                    categorized["Scooter"].append(v)
        print("\nCars:")
        for car in categorized["Car"]:
            print(" ", car)
        if not categorized["Car"]:
            print("  No cars available")
        print("\nScooters:")
        for s in categorized["Scooter"]:
            print(" ", s)
        if not categorized["Scooter"]:
            print("  No scooters available")
    # ---------- UC-10: Fleet Analytics -----------------
    def fleet_analytics(self):
        status_count = {
            "Available": 0,
            "On Trip": 0,
            "Under Maintenance": 0
        }
        for vehicles in self.hubs.values():
            for v in vehicles:
                status = v.get_status()
                if status in status_count:
                    status_count[status] += 1
        print("\nFleet Analytics Summary")
        print("-----------------------")
        for status, count in status_count.items():
            print(f"{status}: {count}")
    # ---------- UC-11: Sort Alphabetically -----------------
    def sort_vehicles_in_hub(self, hub_name: str):
        if hub_name not in self.hubs:
            print("Hub not found")
            return
        vehicles = self.hubs[hub_name]
        if not vehicles:
            print("No vehicles in this hub to sort")
            return
        vehicles.sort(key=lambda v: v.model)
        print(f"\nVehicles in '{hub_name}' sorted by model name:")
        for v in vehicles:
            print(" ", v)
    # ---------- UC-12: Advanced Sorting -----------------
    def sort_by_battery(self):
        all_vehicles = []
        for vehicles in self.hubs.values():
            all_vehicles.extend(vehicles)
        if not all_vehicles:
            print("No vehicles available")
            return
        sorted_list = sorted(all_vehicles, key=lambda v: v.get_battery(), reverse=True)
        print("\nVehicles Sorted by Battery (High → Low):")
        for v in sorted_list:
            print(" ", v)
    def sort_by_price(self):
        all_vehicles = []
        for vehicles in self.hubs.values():
            all_vehicles.extend(vehicles)
        if not all_vehicles:
            print("No vehicles available")
            return
        sorted_list = sorted(all_vehicles, key=lambda v: v.get_price(), reverse=True)
        print("\nVehicles Sorted by Fare Price (High → Low):")
        for v in sorted_list:
            print(" ", v)
    # ---------- UC-13: CSV Save / Load -----------------
    def save_to_csv(self, filename="fleet_data.csv"):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["hub", "vehicle_id", "model", "battery",
                             "status", "price", "extra", "type"])
            for hub, vehicles in self.hubs.items():
                for v in vehicles:
                    if isinstance(v, ElectricCar):
                        extra = v.seating_capacity
                        vtype = "car"
                    else:
                        extra = v.max_speed
                        vtype = "scooter"
                    writer.writerow([hub, v.vehicle_id, v.model, v.get_battery(),
                                     v.get_status(), v.get_price(), extra, vtype])
        print("Fleet data saved to CSV")
    def load_from_csv(self, filename="fleet_data.csv"):
        try:
            with open(filename, "r") as f:
                rows = csv.DictReader(f)
                for row in rows:
                    hub = row["hub"]
                    if hub not in self.hubs:
                        self.hubs[hub] = []
                    vid = row["vehicle_id"]
                    model = row["model"]
                    battery = float(row["battery"])
                    status = row["status"]
                    price = float(row["price"])
                    extra = int(row["extra"])
                    vtype = row["type"]
                    if vtype == "car":
                        vehicle = ElectricCar(vid, model, battery, status, price, extra)
                    else:
                        vehicle = ElectricScooter(vid, model, battery, status, price, extra)

                    self.hubs[hub].append(vehicle)
            print("Fleet data loaded from CSV")
        except FileNotFoundError:
            print("CSV file not found, starting fresh")
    # ---------- UC-14: JSON Save / Load -----------------
    def save_to_json(self, filename="fleet_data.json"):
        data = {}
        for hub, vehicles in self.hubs.items():
            data[hub] = []
            for v in vehicles:
                entry = {
                    "vehicle_id": v.vehicle_id,
                    "model": v.model,
                    "battery": v.get_battery(),
                    "status": v.get_status(),
                    "price": v.get_price(),
                }
                if isinstance(v, ElectricCar):
                    entry["type"] = "car"
                    entry["extra"] = v.seating_capacity
                else:
                    entry["type"] = "scooter"
                    entry["extra"] = v.max_speed
                data[hub].append(entry)
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print("Fleet data saved to JSON")
    def load_from_json(self, filename="fleet_data.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
            for hub, vehicles in data.items():
                if hub not in self.hubs:
                    self.hubs[hub] = []
                for v in vehicles:
                    vid = v["vehicle_id"]
                    model = v["model"]
                    battery = float(v["battery"])
                    status = v["status"]
                    price = float(v["price"])
                    extra = int(v["extra"])
                    vtype = v["type"]
                    if vtype == "car":
                        vehicle = ElectricCar(vid, model, battery, status, price, extra)
                    else:
                        vehicle = ElectricScooter(vid, model, battery, status, price, extra)
                    self.hubs[hub].append(vehicle)
            print("Fleet data loaded from JSON")
        except FileNotFoundError:
            print("JSON file not found, starting fresh")
