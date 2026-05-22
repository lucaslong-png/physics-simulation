class lazy_susan:
    __init__(self, radius, mass, ang_spd, direction):
        r = radius
        m = mass
        w0 = ang_spd
        dir = direction
        I = 1/2 * mass * radius ** 2
#assumed uniform mass distribution

    calcAngularMomentum():
        return I * w0

    calcEnergy():
        return 1 / 2 * I * w0 ** 2
