# input_processing.py
# Behzad Fuladpanjeh Hojaghan, ENSF 692 Spring 2025
#
# A class to get status of the traffic light (green, yellow, red), pedestrian (yes, no), 
# and vehicle (yes, no) then make an apropriate car driving action (STOP, Caution, Proceed)
# 

class Sensor:
    # Initialize sensor with default values:
    # Traffic light = green, no pedestrian, and no vehicle detected.
    def __init__(self):
        self.traffic_light = "green"
        self.pedestrian = "no" 
        self.vehicle = "no"

    # Updates a specific sensor value based on the user's selected input option.
    # Option 1: traffic light, Option 2: pedestrian, Option 3: vehicle.
    def update_status(self, option):
        if option == 1:
            light = input("Enter traffic light color (green/yellow/red): ")
            if light in ["green", "yellow", "red"]:
                self.traffic_light = light # Update traffic light status
            else:
                print("Invalid traffic light color. Please try again.")
        elif option == 2:
            pedestrian = input("Is a pedestrian detected? (yes/no): ")
            if pedestrian in ["yes", "no"]:
                self.pedestrian = pedestrian # Update pedestrian status
            else:
                print("Invalid pedestrian status. Please try again.")
        elif option == 3:
            vehicle = input("Is a vehicle detected? (yes/no): ")
            if vehicle in ["yes", "no"]:
                self.vehicle = vehicle # Update vehicle status
            else:
                print("Invalid vehicle status. Please try again.")

# Determine and display appropriate driving action based on current sensor values.
# STOP if the traffic light is red or a pedestrian/vehicle is detected.
# Caution if the traffic light is yellow and no pedestrian/vehicle is detected.
# Otherwise Proceed.
def print_message(sensor):

    if sensor.traffic_light == "red" or sensor.pedestrian == "yes" or sensor.vehicle == "yes":
        print("STOP")
    elif sensor.traffic_light == "yellow":
        print("Caution")
    else:
        print("Proceed")
    # Displays current status of sensors
    print("\nTraffic light:", sensor.traffic_light,  " , Pedestrian:", sensor.pedestrian, " , Vehicle:", sensor.vehicle, "\n")

# Main function to run  Car Vision Detector Processing Program.
# Continuously prompts the user to update sensor inputs.
# Displays the driving action based on updated sensor values. 
# Throw an exception if an invalid input is entered by the user
def main():
    # Prints program title
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    sensor = Sensor()
    # Loop continuously until user chooses to exit (option 0)
    while True:
        print("Are changes detected in the vision input")
        print("Select 1 for traffic light, 2 for pedestrian, 3 for vehicle, or 0 to end the program")
 
        try: # Get and validate user input
            choice = int(input("Enter your choice: "))
            if choice == 0:
                print("Program ended.")
                break
            elif choice in [1, 2, 3]:
                sensor.update_status(choice)
                print_message(sensor)
            else:
                print("Invalid option. You must select 1, 2, 3, or 0 to exit.")
        except ValueError:
            print("Invalid input. You must select 1, 2, 3, or 0 to exit.")


# Conventional Python code for running main within a larger program
if __name__ == '__main__':
    main()