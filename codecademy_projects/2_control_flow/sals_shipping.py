# This program calculates shipping costs based on weight using different shipping methods.


weight = 41.5

#Ground shipping
if weight <= 2:
  cost_ground = weight * 1.50 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <= 10:
  cost_ground = weight * 4 + 20
else: 
  cost_ground = weight * 4.75 + 20

print(cost_ground)

premium_ground_shipping = 125.00
print(premium_ground_shipping)

#DRONE SHIPPING

if weight <=2:
  cost_drone = weight * 4.50 
elif weight <6:
  cost_drone = weight * 9.00
elif weight <10: 
  cost_drone = weight * 12.00
else: 
  cost_drone = weight * 14.25
print(cost_drone)