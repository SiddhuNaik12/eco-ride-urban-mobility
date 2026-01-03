from vehicle import Vehicle

def main() -> None:
    print("Welocme to Eco-Ride Urban Mobility System")
    #UC1: Basic fleet setup
    vehicle_1=Vehicle("EV101","Ather 450X",85.5)
    print("Vehicle Created successfully!")
    print(vehicle_1)
if __name__=='__main__':
    main()