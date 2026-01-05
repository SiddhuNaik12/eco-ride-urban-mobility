from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self,vid: str,model: str,battery: float,status: str, price: float):
        self.vehicle_id = vid
        self.model = model
        self.__battery_percentage = None
        self.__maintenance_status = status
        self.__rental_price = price
        self.update_battery(battery)
    # -------- getters --------
    def get_battery(self) -> float:
        return self.__battery_percentage
    def get_status(self) -> str:
        return self.__maintenance_status
    def get_price(self) -> float:
        return self.__rental_price
    # -------- setters --------
    def update_battery(self, battery: float) -> None:
        if battery < 0 or battery > 100:
            raise ValueError("Invalid battery value")
        self.__battery_percentage = battery
    def update_status(self, status: str) -> None:
        self.__maintenance_status = status
    def update_price(self, price: float) -> None:
        if price <= 0:
            raise ValueError("Invalid price")
        self.__rental_price = price
    # -------- abstraction --------
    @abstractmethod
    def calculate_trip_cost(self, distance: float) -> float:
        pass
    def __str__(self) -> str:
        return (
            f"Vehicle ID: {self.vehicle_id}, "
            f"Model: {self.model}, "
            f"Battery: {self.__battery_percentage}%, "
            f"Status: {self.__maintenance_status}, "
            f"Base Price: {self.__rental_price}"
        )
class ElectricCar(Vehicle):
    def __init__(self,vid: str,model: str,battery: float,status: str,price: float,seats: int):
        super().__init__(vid, model, battery, status, price)
        self.seating_capacity = seats
    #Polymorphic behaviour
    def calculate_trip_cost(self, distance: float) -> float:
        return 5.0+(0.5*distance)
    def __str__(self) -> str:
        return super().__str__() + f", Seats: {self.seating_capacity}"

class ElectricScooter(Vehicle):
    def __init__(self,vid: str,model: str,battery: float,status: str,price: float,speed_limit: int):
        super().__init__(vid, model, battery, status, price)
        self.max_speed_limit = speed_limit
    #Polymorphic behaviour
    def calculate_trip_cost(self, minutes: float) -> float:
        return 1.0 * (0.15*minutes)
    def __str__(self) -> str:
        return super().__str__() + f", Speed Limit: {self.max_speed_limit} km/h"
