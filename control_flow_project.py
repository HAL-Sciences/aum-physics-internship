weight = 41.5 # In pounds

# Ground Shipping
if weight <= 2:
  print("The regular ground shipping cost for this is: " + str (round(1.5 * weight + 20, 2)) )
elif weight <= 6:
  print("The regular ground shipping cost for this is: " + str (round(3 * weight + 20, 2)) )
elif weight <= 10:
  print("The regular ground shipping cost for this is: " + str (round(4 * weight + 20, 2)) )
elif weight >= 10:
  print("The regular ground shipping cost for this is: " + str (round(4.75 * weight + 20, 2)) )
else:
  print("Cannot calculate the regular ground shipping cost. Please enter a valid weight.")

premium_ground_shipping_cost = 125.00
print("The premium ground shipping cost for this is: " + str(premium_ground_shipping_cost) )

# Drone Shipping
if weight <= 2:
  print("The drone shipping cost for this is: " + str (round(4.5 * weight, 2)) )
elif weight <= 6:
  print("The drone shipping cost for this is: " + str (round(9.0 * weight, 2)) )
elif weight <= 10:
  print("The drone shipping cost for this is: " + str (round(12.0 * weight, 2)) )
elif weight >= 10:
  print("The drone shipping cost for this is: " + str (round(14.25 * weight, 2)) )
else:
  print("Cannot calculate the drone shipping cost. Please enter a valid weight.")

# I noticed that If I were to change it so that instead of printing the cost, these expressions could define variables that represent the cost
# for example, instead of printing the weight, I could set what ground_shipping_cost is equal to, and use that to print the cost

# this would allow me to do this:
# if ground_shipping_cost <= drone_shipping_cost and ground_shipping_cost <= premium_ground_shipping_cost:
   # print("It would be cheapest to ship with regular ground shipping!")
# elif drone_shipping_cost <= ground_shipping_cost and drone_shipping_cost <= premium_ground_shipping_cost:
    # print("It would be cheapest to ship with drone shipping!")
# else:
    # print("You should ship this with premium ground shipping!")