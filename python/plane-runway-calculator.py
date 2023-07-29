timePassed = 0

planeVelocity = 70 # The planes velocity needed to takeoff m/s
planeAcceleration = 30 # The planes takeoff acceleration meters

minimumTakeoffRunway = 0 


# Calculations
timePassed = planeVelocity / planeAcceleration 
planeAcceleration = planeVelocity / timePassed 
minimumTakeoffRunway = 1 / 2 * (planeAcceleration * timePassed) ** 2 
print(minimumTakeoffRunway)

