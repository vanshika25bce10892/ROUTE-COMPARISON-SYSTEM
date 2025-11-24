#Smart Route Cost and Time Calculator
def calculate_route(distance,milage,fuel_price,speed):
    fuel_needed = distance/milage
    cost = fuel_needed*fuel_price
    time = distance/speed
    return fuel_needed,cost,time
print("---Route Comparison Tool---")
# Input for Route 1
print("\nEnter details for Route 1")
d1 = float(input("Distance (km): "))
m1 = float(input("Mileage (km/litre): "))
fp1 = float(input("Fuel Price: "))
s1 = float(input("Speed (km/hr): "))

fuel1, cost1, time1 = calculate_route(d1, m1, fp1, s1)

# Input for Route 2
print("\nEnter details for Route 2")
d2 = float(input("Distance (km): "))
m2 = float(input("Mileage (km/litre): "))
fp2 = float(input("Fuel Price: "))
s2 = float(input("Speed (km/hr): "))

fuel2, cost2, time2 = calculate_route(d2, m2, fp2, s2)

print("\n----- RESULTS -----")
print(f"Route 1 -> Fuel: {fuel1:.2f} L, Cost: ₹{cost1:.2f}, Time: {time1:.2f} hrs")
print(f"Route 2 -> Fuel: {fuel2:.2f} L, Cost: ₹{cost2:.2f}, Time: {time2:.2f} hrs")

print("\n----- BEST ROUTE -----")
if cost1 < cost2:
    print("Cheaper Route: Route 1")
else:
    print("Cheaper Route: Route 2")

if time1 < time2:
    print("Faster Route: Route 1")
else:
    print("Faster Route: Route 2")
