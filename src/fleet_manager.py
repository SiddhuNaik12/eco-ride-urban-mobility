import csv
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
    def sort_by_battery(self) -> None:
        all_vehicles = []

        # take all vehicles from all hubs
        for vehicles in self.hubs.values():
            all_vehicles.extend(vehicles)

        if not all_vehicles:
            print("No vehicles available to sort")
            return

        # sort in descending order using lambda
        sorted_battery = sorted(all_vehicles, key=lambda v: v.get_battery(), reverse=True)

        print("\nVehicles Sorted by Battery Level (High → Low):")
        for v in sorted_battery:
            print(" ", v)
    def sort_by_price(self) -> None:
        all_vehicles = []

        # collect all vehicles from all hubs
        for vehicles in self.hubs.values():
            all_vehicles.extend(vehicles)

        if not all_vehicles:
            print("No vehicles available to sort")
            return

        # sort in descending order by fare price
        sorted_price = sorted(all_vehicles, key=lambda v: v.get_price(), reverse=True)

        print("\nVehicles Sorted by Fare Price (High → Low):")
        for v in sorted_price:
            print(" ", v)
    def save_to_csv(self,filename: str="fleet_data.csv")->None:
        with open(filename,mode="w",newline="") as file:
            writer=csv.writer(file)
            #header row
            writer.writerow([
                "hub_name","vehicle_id","model","battery",
                "status","price","extra","type"
            ])
            #write all vehicles
            for hub, vehicles in self.hubs.items():
                for v in vehicles:
                    if v.__class__.__name__=="ElectricCar":
                        extra=v.seating_capacity
                        vtype="car"
                    else:
                        extra=v.max_speed
                        vtype="scooter"
                    write.writerow([
                        hub,v.vehicle_id,v.model,
                        v.get_battery(),v.get_status(),
                        v.get_price(),extra,vtype
                    ])
            print("Fleet data saved to CSV")  
    def load_from_csv(self, filename: str = "fleet_data.csv") -> None:
        try:
            with open(filename, mode="r") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    hub = row["hub_name"]
                    if hub not in self.hubs:
                        self.hubs[hub] = []

                    vid = row["vehicle_id"]
                    model = row["model"]
                    battery = float(row["battery"])
                    status = row["status"]
                    price = float(row["price"])
                    extra = row["extra"]
                    vtype = row["type"]

                    if vtype == "car":
                        from vehicle import ElectricCar
                        vehicle = ElectricCar(vid, model, battery, status, price, int(extra))
                    else:
                        from vehicle import ElectricScooter
                        vehicle = ElectricScooter(vid, model, battery, status, price, int(extra))

                    self.hubs[hub].append(vehicle)

            print("Fleet data loaded from CSV")

        except FileNotFoundError:
            print("CSV file not found, starting with empty fleet")

