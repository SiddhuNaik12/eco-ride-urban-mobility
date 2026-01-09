from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, vehicle_id: str, model: str, battery: float,
                 status: str, rental_price: float):
        self.vehicle_id = vehicle_id
        self.model = model
        # private attributes
        self.__battery_percentage = None
        self.set_battery_percentage(battery)
        self.__maintenance_status = status
        self.__rental_price = rental_price
    # ------------ Encapsulation Setters & Getters -------------
    def set_battery_percentage(self, value: float):
        if value < 0 or value > 100:
            print("Battery percentage should be between 0 and 100")
        else:
            self.__battery_percentage = value
    def get_battery(self) -> float:
        return self.__battery_percentage
    def get_status(self) -> str:
        return self.__maintenance_status
    def get_price(self) -> float:
        return self.__rental_price
    # ---------------- Abstract Method (UC-4) -------------------
    @abstractmethod
    def calculate_trip_cost(self, distance_or_minutes: float) -> float:
        pass
    # ---------------- Equality Check (UC-7) --------------------
    def __eq__(self, other) -> bool:
        if not isinstance(other, Vehicle):
            return False
        return self.vehicle_id == other.vehicle_id
    # ---------------- String Printing (UC-11) ------------------
    def __str__(self) -> str:
        return (
            f"Vehicle ID: {self.vehicle_id}, Model: {self.model}, "
            f"Battery: {self.__battery_percentage}%, "
            f"Status: {self.__maintenance_status}, "
            f"Base Price: ₹{self.__rental_price}"
        )
# ---------------- Electric Car --------------------
class ElectricCar(Vehicle):
    def __init__(self, vehicle_id, model, battery, status, price, seating_capacity):
        super().__init__(vehicle_id, model, battery, status, price)
        self.seating_capacity = seating_capacity
    def calculate_trip_cost(self, distance: float) -> float:
        return 5.0 + (0.50 * distance)
    def __str__(self):
        return super().__str__() + f", Seats: {self.seating_capacity}"
# ---------------- Electric Scooter --------------------
class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery, status, price, max_speed):
        super().__init__(vehicle_id, model, battery, status, price)
        self.max_speed = max_speed
    def calculate_trip_cost(self, minutes: float) -> float:
        return 1.0 + (0.15 * minutes)
    def __str__(self):
        return super().__str__() + f", Speed Limit: {self.max_speed} km/h"
