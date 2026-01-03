class Vehicle:
    def __init__(
        self,
        vehicle_id: str,
        model: str,
        battery_percentage: float,
        maintenance_status: str,
        rental_price: float
    ):
        self.vehicle_id = vehicle_id
        self.model = model

        # private attributes
        self.__battery_percentage = None
        self.__maintenance_status = maintenance_status
        self.__rental_price = rental_price

        # call setter for validation
        self.set_battery_percentage(battery_percentage)

    # -------- GETTERS --------

    def get_battery_percentage(self) -> float:
        return self.__battery_percentage

    def get_maintenance_status(self) -> str:
        return self.__maintenance_status

    def get_rental_price(self) -> float:
        return self.__rental_price

    # -------- SETTERS --------

    def set_battery_percentage(self, battery_percentage: float) -> None:
        if 0 <= battery_percentage <= 100:
            self.__battery_percentage = battery_percentage
        else:
            raise ValueError("Battery percentage must be between 0 and 100")

    def set_maintenance_status(self, status: str) -> None:
        self.__maintenance_status = status

    def set_rental_price(self, price: float) -> None:
        if price > 0:
            self.__rental_price = price
        else:
            raise ValueError("Rental price must be greater than 0")

    def __str__(self) -> str:
        return (
            f"Vehicle ID: {self.vehicle_id}, "
            f"Model: {self.model}, "
            f"Battery: {self.__battery_percentage}%, "
            f"Maintenance: {self.__maintenance_status}, "
            f"Rental Price: ₹{self.__rental_price}"
        )
