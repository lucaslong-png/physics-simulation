Web VPython 3.2
import math
class lazy_susan:
    __init__(self, rad, mass, ang_spd, direction):
        r = rad
        m = mass
        w0 = ang_spd
        dir = direction
        I = 1/2 * mass * radius ** 2
        disk = circle(pos = vec(0, 0), radius = r, np = 256)



#assumed uniform mass distribution

    calcAngularMomentum():
        return I * w0

    calcEnergy():
        return 1 / 2 * I * w0 ** 2


class bug:
    _init_(self, mass, speed, acceleration, distance, angle):
        m = mass
        spd = speed
        accel = acceleration
        dist = distance
        ang = angle #from radial distance
        ladybug = circle(radius = 0.1, np = 256, pos = (vec(0,0) + distance * vec(math.cos(angle), math.sin(angle))

    calcAngularMomentum():
        return m * spd * dist * sin(angle)

    calcEnergy():
        return 1 / 2 * m * spd ** 2


setup():
    
