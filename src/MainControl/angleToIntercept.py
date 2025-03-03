import numpy as np

# Uses the data from the camera to determine the angle the robot needs to turn to intercept the other robot.
def angleToIntercept(distance, theta0, theta1, runnerSpeed, chaserSpeed):
    # Check with lam on the logic
    if (theta0 > 0): # Robot is on the left
        if(theta1 > 90 or theta1 > 270): # Robot is going left
            theta = 180 + theta0 - theta1
        else:
            theta = theta1 - theta0
    else: # Robot is on the right
        if(theta1 > 90 or theta1 > 270): # Robot is going left
            theta = 180 + theta0 + theta1
        else:
            theta = theta0 - theta1
    theta = np.deg2rad(theta)
    theta0 = np.deg2rad(theta0)
    theta1 = np.deg2rad(theta1)
    b = 2*distance*runnerSpeed*np.cos(theta)
    a = np.power(chaserSpeed, 2)-np.power(runnerSpeed, 2)
    c = np.power(distance,2)
    time = (-b+np.sqrt(np.power(b,2)+4*a*c))/(2*a)
    # D = (cos(theta0)*d, sin(theta0)*d)
    Dy = np.sin(theta0)*distance
    # VR = (cos(theta1)*runnerSpeed, sin(theta1)*runnerSpeed)
    VRy = np.sin(theta1)*runnerSpeed
    y = (Dy+VRy*time)/time
    print("{} {}".format(y,chaserSpeed))
    angle = np.arccos(y/chaserSpeed)
    angle = np.rad2deg(angle)
    return angle
