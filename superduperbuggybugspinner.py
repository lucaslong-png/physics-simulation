Web VPython 3.2
f = 60 #fps
dt = 1 / f
running = False #boolean
totalAngularMomentum = 0
ccwBug = False

class lazy_susan:
    def __init__(self, rad, mass, ang_vel):
        self.r = rad
        self.m = mass
        self.w = ang_vel
        self.disk = cylinder(pos = vec(0, 0, 0), axis = vec(0, 0, 1), radius = self.r, color = color.white, texture = textures.metal)

    def turn(self):
        global dt
        self.disk.rotate(axis = vec(0, 0, 1), angle = self.w * dt)
#assumed uniform mass distribution

    def calcInertia(self):
        return 0.5 * self.m * self.r ** 2

    def calcAngularMomentum(self):
        return self.calcInertia() * self.w

    def calcEnergy(self):
        return 0.5 * self.calcInertia() * self.w ** 2

    def updateCylinder(self):
        self.disk.radius = self.r

class bug:
    def __init__(self, mass, ang_vel, deceleration, distance, angle):
        self.m = mass
        self.avel = ang_vel
        self.decel = deceleration
        self.dist = distance
        self.ang = angle #from positive x axis
        self.ladybug = cylinder(pos = vec(self.dist * cos(angle), self.dist * sin(angle), 1), axis = vec(0, 0, 1), radius = 0.05, length = 0.01, color = color.red)


    def calcInertia(self):
        return self.m * self.dist ** 2

    def calcAngularMomentum(self):
        return self.calcInertia() * self.avel

    def calcEnergy(self):
        return 0.5 * self.m * (self.avel * self.dist) ** 2

    def turn(self, disk):
        global dt
        self.ang += disk.w * dt + self.avel * dt
        while (self.ang > 2 * pi):
            self.ang -= 2 * pi
        while (self.ang < 0):
            self.ang += 2 * pi
        self.ladybug.pos = vec(self.dist * cos(self.ang), self.dist * sin(self.ang), 1)



    def updateCylinder(self):
        self.ladybug.pos = vec(self.dist * cos(self.ang), self.dist * sin(self.ang), 1)


s = lazy_susan(1, 5, 1)
b = bug(1, 1, 0, 0, 0)


def update_mass1(k):
    s.m = k.value
    s.updateCylinder()


mass1Slider = slider(bind = update_mass1, min = 0.01, max = 1, step = 0.01, value = 0.66)
scene.append_to_caption('mass of disk (kg) \n')

def update_mass2(k):
    b.m = k.value
    b.updateCylinder()


mass2Slider = slider(bind = update_mass2, min = 0.01, max = 0.3, step = 0.01, value = 0.17)
scene.append_to_caption('mass of bug (kg) \n')


def update_disk_initial_angular_velocity(k):
    s.w = k.value
    s.updateCylinder()

angVel1Slider = slider(bind = update_disk_initial_angular_velocity, min = -15, max = 15, step = 0.1, value = 2.8)
scene.append_to_caption('disk initial angular velocity (rad/s) \n')


def update_bug_initial_angular_velocity(k):
    b.avel = k.value
    b.updateCylinder()


angVel2Slider = slider(bind = update_bug_initial_angular_velocity, min = -15, max = 15, step = 0.1, value = 13.3)
scene.append_to_caption('bug initial angular velocity (rad/s) \n')


def update_radius1(k):
    s.r = k.value
    s.updateCylinder()


radius1Slider = slider(bind = update_radius1, min = 0.1, max = 1, step = 0.01, value = 0.15)
scene.append_to_caption('disk radius (m) \n')


def update_deceleration(k):
    b.decel = k.value
    b.updateCylinder()


deceleration_slider = slider(bind = update_deceleration, min = 0.00, max = 1, step = 0.01, value = 0)
scene.append_to_caption('bug deceleration (rad/s^2) \n')


def update_radial_distance(k):
    b.dist = k.value
    b.updateCylinder()


radial_distance_slider = slider(bind = update_radial_distance, min = 0.01, max = 1, step = 0.01, value = s.r)
scene.append_to_caption('bug radial distance (m) \n')


def update_initial_angle(k):
    b.ang = k.value
    b.updateCylinder()


initial_angle_slider = slider(bind = update_initial_angle, min = 0, max = 2 * pi, value = s.r)
scene.append_to_caption('bug initial angle (radians) \n')


def start_simulation():
    setup()


startButton = button(bind = start_simulation, text = 'start simulation', pos = scene.title_anchor)

def reset():
    running = False
    s.disk.visible = False
    b.ladybug.visible = False
    s = lazy_susan(1, 5, 1)
    b = bug(1, 1, 0, 0, 0)
    enableWidgets()

resetButton = button(bind = reset, text = 'reset', pos = scene.title_anchor)

#finalAngVel = wtext(text = ...)
def disableWidgets():
    mass1Slider.disabled = True
    mass2Slider.disabled = True
    angVel1Slider.disabled = True
    angVel2Slider.disabled = True
    radius1Slider.disabled = True
    deceleration_slider.disabled = True
    radial_distance_slider.disabled = True
    initial_angle_slider.disabled = True
    startButton.disabled = True

def enableWidgets():
    mass1Slider.disabled = False
    mass2Slider.disabled = False
    angVel1Slider.disabled = False
    angVel2Slider.disabled = False
    radius1Slider.disabled = False
    deceleration_slider.disabled = False
    radial_distance_slider.disabled = False
    initial_angle_slider.disabled = False
    startButton.disabled = False




def setup():
    global dt, f, running, s, b, totalAngularMomentum, ccwBug
    rate(f)
    dt = 1/f
    running = True
    disableWidgets()
    if (b.avel < 0):
        ccwBug = True
    totalAngularMomentum = sfinal.calcAngularMomentum() + bfinal.calcAngularMomentum()


def setSpeed(frequency):
    global dt
    global f
    rate(frequency)
    f = frequency
    dt = 1/f

def tick():
    global dt, sfinal, bfinal
    s.turn()
    b.turn(s)
    if (ccwBug):
        b.avel += b.decel * dt
    else:
        b.avel -= b.decel * dt
    diskAngularMomentum = totalAngularMomentum - b.calcAngularMomentum()
    s.w = diskAngularMomentum / s.calcInertia()

def beforeSimStartsTick():
    s.turn()
    b.turn(s)



while True:
    rate(f)
    if (running):
        tick()
        if ((ccwBug and b.avel >= 0) or ((not ccwBug) and b.avel <= 0)):
            running = False
    else:
      #  beforeSimStartsTick()
