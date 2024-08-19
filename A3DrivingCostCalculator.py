# CS1400 Assignment 3: Driving Cost Calculator by Lucy Leary #


# Calculates the total cost of a road trip with a gas vehicle.
def calculate_gas_vehicle_trip_cost(trip_length_miles, vehicle_miles_per_gallon, cost_per_gallon_gas):
    return trip_length_miles / vehicle_miles_per_gallon * cost_per_gallon_gas


# Calculates the total cost of a road trip with an electric vehicle.
def calculate_electric_vehicle_trip_cost(trip_length_miles, vehicle_watt_hrs_per_mile, cost_per_kilowatt_hr):
    return vehicle_watt_hrs_per_mile / 1000 * trip_length_miles * cost_per_kilowatt_hr


def main():
    cost_per_gallon_gas = float(input("Type the cost of a gallon of gas: "))
    cost_per_kilowatt_hr = float(input("Type the cost of a kilowatt hour of electricity: "))

    gas_car_miles_per_gallon = 25.1
    gas_truck_miles_per_gallon = 14.2
    electric_car_watt_hrs_per_mile = 230.7

    for trip_length_miles in range(50, 501, 50):
        gas_car_cost = calculate_gas_vehicle_trip_cost(trip_length_miles, gas_car_miles_per_gallon, cost_per_gallon_gas)
        truck_cost = calculate_gas_vehicle_trip_cost(trip_length_miles, gas_truck_miles_per_gallon, cost_per_gallon_gas)
        electric_car_cost = calculate_electric_vehicle_trip_cost(trip_length_miles, electric_car_watt_hrs_per_mile,
                                                                 cost_per_kilowatt_hr)
        print("For a trip of " + str(trip_length_miles) + " miles, the costs are: truck $" + str(round(truck_cost)) +
              ", gas car $" + str(round(gas_car_cost)) + ", electric car $" + str(round(electric_car_cost)) + ".")


if __name__ == "__main__":
    main()
