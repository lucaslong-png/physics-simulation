Web VPython 3.2
import math
f = 60 #fps
dt = 1 / f
class lazy_susan:
    __init__(self, rad, mass, ang_spd, direction):
        r = rad
        m = mass
        w = ang_spd
        dir = direction #int, either -1 or 1
        I = 1/2 * mass * radius ** 2
        disk = cylinder(pos = vec(0, 0, 0), axis = vec(0, 0, 1), radius = r, color = color.white, texture = textures.metal)

    turn():
        disk.color = vector(1, 0, 0)
        disk.rotate(axis = vec(0, 0, 1), angle = w * dt)
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

lazy_susan s = lazy_susan(s, 1, 5, 1, 1)
bug b = bug(b, 1, 1, 0, 0, 0)

update_mass1(k):
    s.m = k

mass1Slider = slider(bind = updateMass1, min = 0.01, max = 1, step = 0.01, value = 0.66)

update_mass2(k):
    b.m = k

mass2Slider = slider(bind = updateMass1, min = 0.01, max = 0.3, step = 0.01, value = 0.17)

update_initial_angular_velocity(k):
    s.w = k

mass2Slider = slider(bind = updateMass1, min = 0.01, max = 0.3, step = 0.01, value = 0.17)



setup():
    rate(f)
    dt = 1/f

setSpeed(frequency):
    rate(frequency)
    f = frequency

tick():

    
