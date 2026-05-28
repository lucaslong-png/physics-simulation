Web VPython 3.2
import math
f = 60 #fps
dt = 1 / f
class lazy_susan:
    def __init__(self, rad, mass, ang_vel):
        r = rad
        m = mass
        w = ang_vel
        I = 1/2 * mass * radius ** 2
        disk = cylinder(pos = vec(0, 0, 0), axis = vec(0, 0, 1), radius = r, color = color.white, texture = textures.metal)

    def turn():
        disk.rotate(axis = vec(0, 0, 1), angle = w * dt)
#assumed uniform mass distribution


    def calcAngularMomentum():
        return I * w0

    def calcEnergy():
        return 1 / 2 * I * w0 ** 2


class bug:
    def _init_(self, mass, ang_vel, acceleration, distance, angle):
        m = mass
        vel = ang_vel
        accel = acceleration
        dist = distance
        ang = angle #from radial distance
        ladybug = circle(radius = 0.02, np = 256, pos = (vec(0,0) + distance * vec(math.cos(angle), math.sin(angle))

    def calcAngularMomentum():
        return m * spd * dist * sin(angle)

    def calcEnergy():
        return 1 / 2 * m * (ang_vel / distance) ** 2

s = lazy_susan(s, 1, 5, 1)
b = bug(b, 1, 1, 0, 0, 0)

def update_mass1(k):
    s.m = k

mass1Slider = slider(bind = update_mass1, min = 0.01, max = 1, step = 0.01, value = 0.66)

def update_mass2(k):
    b.m = k

mass2Slider = slider(bind = update_mass2, min = 0.01, max = 0.3, step = 0.01, value = 0.17)

def update_disk_initial_angular_velocity(k):
    s.w = k

angVel1Slider = slider(bind = update_disk_initial_angular_velocity, min = -15, max = 15, step = 0.1, value = 2.8)

def update_bug_initial_angular_velocity(k):
    b.w = k

angVel2Slider = slider(bind = update_bug_initial_angular_velocity, min = -15, max = 15, step = 0.1, value = 13.3)

def update_radius1(k):
    s.r = k

radius1Slider = slider(bind = update_radius1, min = 0.1, max = 1, step = 0.01, value = 0.15)

def update_deceleration(k):
    b.accel = k

deceleration_slider = slider(bind = update_deceleration, min = 0.00, max = 1, step = 0.01, value = 0)

def update_radial_distance(k):
    b.dist = k

radial_distance_slider = slider(bind = update_radial_distance, min = 0.01, max = s.r, step = 0.01, value = s.r)




def setup():
    rate(f)
    dt = 1/f

def setSpeed(frequency):
    rate(frequency)
    f = frequency

def tick():


    
