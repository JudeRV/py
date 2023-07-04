########################################################
########################################################
#
#Your name: Jude Vargas
#
#Names of people you consulted
#for this assignment(if None, say None): None
#
#I affirm that I have not violated the
#Academic Integrity policies detailed in the syllabus
#
########################################################
########################################################

def main():
    """
    Function main prompts the user for information about their travels, then prints their travel & arrival times

    Parameters: None
    
    Returns: None
    """

    # Prints greeting, prompts the user for each input, and stores each of them as integers
    print("Welcome to the travel advisor program.")
    current_hours = int(input("Enter current time, the hours part, using a 24-hour format: "))
    current_mins = int(input("Enter current time, the minutes part: "))
    distance = int(input("Enter distance to destination in miles: "))
    speed = int(input("Enter speed in miles/hour: "))

    # Calculates the time it will take to travel the given distance at the given speed
    travel_hours = distance // speed
    travel_mins = round(distance / speed % 1 * 60)

    # Calculates the arrival time from the current and travel times
    dest_hours = current_hours + travel_hours + (current_mins + travel_mins) // 60
    dest_mins = (current_mins + travel_mins) % 60 

    #Prints the trip report including the travel and arrival times
    print("\n\nHere is the trip report:\n---\n")
    print(f"Current time is {format(current_hours, '02d')}:{format(current_mins, '02d')}")
    print(f"Distance to destination is {distance} miles")
    print(f"Travel speed is {speed} miles/hour")
    print(f"Travel time remaining: {travel_hours} hours and {travel_mins} minutes")
    print(f"You will reach your destination at {format(dest_hours, '02d')}:{format(dest_mins, '02d')}")

# Executes the main function only if the file is being executed directly
if __name__ == "__main__":
    main()