Web VPython 3.2
f = 60 #fps
dt = 1 / f
running = True #boolean
class lazy_susan:
    def __init__(self, rad, mass, ang_vel):
        self.r = rad
        self.m = mass
        self.w = ang_vel
        self.I = 1/2 * mass * rad ** 2
        self.disk = cylinder(pos = vec(0, 0, 0), axis = vec(0, 0, 1), radius = self.r, color = color.white, texture = textures.metal)

    def turn(self):
        global dt
        self.disk.rotate(axis = vec(0, 0, 1), angle = self.w * dt)
#assumed uniform mass distribution


    def calcAngularMomentum(self):
        return self.I * self.w

    def calcEnergy(self):
        return 1 / 2 * self.I * self.w ** 2

    def updateCylinder(self):
        global dt
        self.disk.visible = False
        self.disk = cylinder(pos = vec(0, 0, 0), axis = vec(0, 0, 1), radius = self.r, color = color.white, texture = textures.metal)

class bug:
    def __init__(self, mass, ang_vel, deceleration, distance, angle):
        self.m = mass
        self.avel = ang_vel
        self.decel = deceleration
        self.dist = distance
        self.ang = angle #from positive x axis
        self.ladybug = cylinder(pos = self.dist * vec(cos(angle), sin(angle), 0), axis = vec(0, 0, 1), radius = 0.1, color = color.red)

    def calcAngularMomentum(self):
        return self.m * self.dist ** 2 * self.avel

    def calcEnergy(self):
        return 1 / 2 * self.m * (self.avel * self.dist) ** 2

    def turn(self):
        global dt
        self.ladybug.rotate(axis = vec(0, 0, 1), angle = self.avel * dt)
        self.ang += self.avel * dt
        if (self.ang > 2 * pi):
            self.ang -= 2 * pi


    def updateCylinder(self):
        self.ladybug.visible = False
        self.ladybug = cylinder(pos = self.dist * vec(cos(self.ang), sin(self.ang), 0), axis = vec(0, 0, 1), radius = 0.1, color = color.red)


s = lazy_susan(1, 5, 1)
b = bug(1, 1, 0, 0, 0)

def start_simulation():
    setup()
    global running
    running = True

startButton = button(bind = start_simulation, text = 'start simulation', pos = scene.title_anchor)

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
scene.append_to_caption('disk deceleration (rad/s^2) \n')


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






def setup():
    global dt
    global f
    rate(f)
    dt = 1/f

def setSpeed(frequency):
    global dt
    global f
    rate(frequency)
    f = frequency
    dt = 1/f

def tick():
    s.turn()
    b.turn()
    b.avel -= b.decel * dt


#while True:
 #   rate(f)
  #  if (running):
   #     tick()
