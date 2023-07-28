

planeSpeed = 0 # Plane's Current Speed Meters Per Second
planeMass = 1134 # Plane's Current Kilo Newtons
planeAcceleration = (planeMass / planeMass) ** 2 # Plane's Current Acceleration Meters Per Second

runwayLengthTakeoff = 0 # Required Runway Length for Takeoff
runwayLengthLanding = 0 # Required Runway Length for Landing


def minimumRunwayTakeoff(speed, acceleration):
    while True:
        speed += acceleration
        if speed >= 66:
            print("{:.0f} meters needed for takeoff.".format(speed ** 2 / (2 * acceleration)))
            break
minimumRunwayTakeoff(planeSpeed, planeAcceleration)