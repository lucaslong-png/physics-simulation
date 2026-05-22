class bug:
    _init_(self, mass, speed, acceleration, distance, angle):
        m = mass
        spd = speed
        accel = acceleration
        dist = distance
        ang = angle #from radial distance

    calcAngularMomentum():
        return m * spd * dist * sin(angle)

    calcEnergy():
        return 1 / 2 * m * spd ** 2

tan_spd_slider = slider(bind = updateSpd, min = 0, max = 10)
