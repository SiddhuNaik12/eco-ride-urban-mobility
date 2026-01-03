class Vehicle:
    def __init__(self,vehicle_id:str, model: str,battery_percentage:float):
        self.vehicle_id=vehicle_id
        self.model=model
        self.battery_percentage=battery_percentage
    def __str__(self) -> str:
        return( 
            f"Vehicle ID:{self.vehicle_id},"
            f"Model:{self.model},"
            f"Battery: {self.battery_percentage}%"
        )
        
        