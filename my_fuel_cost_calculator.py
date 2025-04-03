# Lesson 3: Operators and Expressions
## Performing Calculations and Making Decisions in Python

my_title = "--------Fuel Cost Calculator--------"
print(my_title)

# Fuel consumption rate
fuel_consumption_rate = 8 / 100 # Liters per kilometer
print(f"Assumed fuel consumption rate is 8 liters per 100 kilometers({fuel_consumption_rate}).")

# Inputs for the user to enter the distance travelled
distance = float(input("Enter the distance in kilometers: "))
print(distance)
# Input for the cost of fuel per liter
fuel_cost_per_liter = float(input("Enter the cost per liter of fuel: "))
print(fuel_cost_per_liter)

# Calculate the total fuel required
total_fuel_required = distance * fuel_consumption_rate
print(f"The total fuel required will be {distance}km X {fuel_consumption_rate}l/km = {total_fuel_required} liters.")

# Calculate the total fuel cost
total_fuel_cost = total_fuel_required * fuel_cost_per_liter
print(f"The total cost of fuel will be {total_fuel_required} X {fuel_cost_per_liter}$ = {total_fuel_cost}$.")