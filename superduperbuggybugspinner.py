Web VPython 3.2
f = 60 #fps
dt = 1 / f
t = 0
running = False
totalAngularMomentum = 0
ccwBug = False
postSimulation = False
scene.userzoom = False
scene.userspin = False
scene.userpan = False
scene.ambient = color.white*0.3


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
        self.ladybug = cylinder(pos = vec(self.dist * cos(angle), self.dist * sin(angle), 1), axis = vec(0, 0, 1), radius = 0.015, length = 0.001, color = vec(0.6,0,0))


    def calcInertia(self):
        return self.m * self.dist ** 2

    def calcAngularMomentum(self, disk):
        return self.calcInertia() * (self.avel + disk.w)

    def calcEnergy(self, disk):
        return 0.5 * self.calcInertia() * (self.avel + disk.w) ** 2

    def turn(self, disk):
        global dt, inshape
        self.ang += disk.w * dt + self.avel * dt
        while (self.ang > 2 * pi):
            self.ang -= 2 * pi
        while (self.ang < 0):
            self.ang += 2 * pi
        self.ladybug.pos = vec(self.dist * cos(self.ang), self.dist * sin(self.ang), 1)
        inshape.pos = self.ladybug.pos



    def updateCylinder(self):
        global inshape
        self.ladybug.pos = vec(self.dist * cos(self.ang), self.dist * sin(self.ang), 1)
        inshape.pos = self.ladybug.pos

s = lazy_susan(0.15, 0.44, -2.8)
b = bug(0.17, 16.1, 0, 0.15, 0)
inshape = cylinder(pos = b.ladybug.pos, axis = vec(0, 0, 1), radius = 0.014, length = 0.001, color = color.red)
scene.autoscale = False
bground = box(pos = vec(0,0,-2), texture = textures.wood, size = vec(9.4,6,1))

directionLabel = label(pos = vector(0, scene.range-0.1, 1), text = 'Note: positive angular velocity values are considered to be in the counterclockwise direction', color = vec(255, 0, 0))
#need to fix

def update_mass1(k):
    s.m = k.value
    s.updateCylinder()
    mass1.text = mass1Slider.value


mass1Slider = slider(bind = update_mass1, min = 0.01, max = 1, step = 0.01, value = 0.44, top = 15)
scene.append_to_caption('mass of disk: ')
mass1 = wtext(text = mass1Slider.value)
scene.append_to_caption(' kg \n')


def update_mass2(k):
    b.m = k.value
    b.updateCylinder()
    mass2.text = mass2Slider.value



mass2Slider = slider(bind = update_mass2, min = 0.01, max = 0.3, step = 0.01, value = 0.17, top = 15)
scene.append_to_caption('mass of bug: ')
mass2 = wtext(text = mass2Slider.value)
scene.append_to_caption(' kg \n')




def update_disk_initial_angular_velocity(k):
    s.w = k.value
    s.updateCylinder()
    angVel1.text = angVel1Slider.value


angVel1Slider = slider(bind = update_disk_initial_angular_velocity, min = -15, max = 15, step = 0.1, value = -2.8, top = 15)
scene.append_to_caption('disk initial angular velocity: ')
angVel1 = wtext(text = angVel1Slider.value)
scene.append_to_caption(' rad/s \n')



def update_bug_initial_angular_velocity(k):
    b.avel = k.value
    b.updateCylinder()
    angVel2.text = angVel2Slider.value


angVel2Slider = slider(bind = update_bug_initial_angular_velocity, min = -20, max = 20, step = 0.1, value = 16.1, top = 15)
scene.append_to_caption('bug initial angular velocity: ')
angVel2 = wtext(text = angVel2Slider.value)
scene.append_to_caption(' rad/s \n')




def update_radius1(k):
    s.r = k.value
    s.updateCylinder()
    radius1.text = radius1Slider.value
    b.dist = radial_distance_slider.value / 100 * s.r
    b.updateCylinder()
    radial_distance.text = b.dist




radius1Slider = slider(bind = update_radius1, min = 0.1, max = 1, step = 0.01, value = 0.15, top = 15)
scene.append_to_caption('disk radius: ')
radius1 = wtext(text = radius1Slider.value)
scene.append_to_caption(' m \n')



def update_deceleration(k):
    b.decel = k.value
    b.updateCylinder()
    deceleration_val.text = deceleration_slider.value


deceleration_slider = slider(bind = update_deceleration, min = 0.00, max = 5, step = 0.01, value = 0, top = 15)
scene.append_to_caption('bug deceleration: ')
deceleration_val = wtext(text = deceleration_slider.value)
scene.append_to_caption(' rad/s² \n')



def update_radial_distance(k):
    b.dist = k.value / 100 * s.r
    b.updateCylinder()
    radial_distance.text = b.dist


radial_distance_slider = slider(bind = update_radial_distance, min = 1, max = 100, step = 1, value = 100, top = 15)
scene.append_to_caption('bug radial distance: ')
radial_distance = wtext(text = s.r)
scene.append_to_caption(' m \n')





def update_initial_angle(k):
    b.ang = k.value
    b.updateCylinder()
    initial_angle_val.text = initial_angle_slider.value


initial_angle_slider = slider(bind = update_initial_angle, min = 0, max = 2 * pi, value = 0, top = 15)
scene.append_to_caption('bug initial angle: ')
initial_angle_val = wtext(text = initial_angle_slider.value)
scene.append_to_caption(' radians \n')

def start_simulation():
    setup()


startButton = button(bind = start_simulation, text = 'start simulation', pos = scene.title_anchor)


g = graph(title = '\nKinetic Energy of System vs. Time', xtitle = 'Time (s)', ytitle = 'Kinetic Energy (J)', ymin = 0)
gc = gcurve(graph = g)


def reset():
    global running, s, b, t, gc, inshape, ccwBug, postSimulation
    running = False
    postSimulation = False
    ccwBug = (b.avel < 0)
    t = 0
    gc.delete()
    s.disk.visible = False
    b.ladybug.visible = False
    inshape.visible = False
    s = lazy_susan(radius1Slider.value, mass1Slider.value, angVel1Slider.value)
    b = bug(mass2Slider.value, angVel2Slider.value, deceleration_slider.value, radial_distance_slider.value / 100 * radius1Slider.value, initial_angle_slider.value)
    inshape = cylinder(pos = b.ladybug.pos, axis = vec(0, 0, 1), radius = 0.014, length = 0.001, color = color.red)
    enableWidgets()

resetButton = button(bind = reset, text = 'reset', pos = scene.title_anchor)

finalAngVel = wtext(text = '\ndisk angular velocity: ' + 0 + ' rad/s')
scene.append_to_caption('\n')
finalAngMomentum = wtext(text = 'total angular momentum: ' + totalAngularMomentum + ' kg m²/s')

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
    ccwBug = False
    rate(f)
    dt = 1/f
    running = True
    disableWidgets()
    if (b.avel < 0):
        ccwBug = True
    totalAngularMomentum = s.calcAngularMomentum() + b.calcAngularMomentum(s)


def setSpeed(frequency):
    global dt
    global f
    rate(frequency)
    f = frequency
    dt = 1/f



def tick():
    global dt, t, g, gc, s, b, ccwBug, finalAngVel, totalAngularMomentum, postSimulation
    s.turn()
    b.turn(s)
    if (not postSimulation):
        if (ccwBug):
            b.avel += b.decel * dt
            s.w -= ((b.decel * b.calcInertia()) / (s.calcInertia() + b.calcInertia())) * dt
        else:
            b.avel -= b.decel * dt
            s.w += ((b.decel * b.calcInertia()) / (s.calcInertia() + b.calcInertia())) * dt
    totalAngularMomentum = b.calcAngularMomentum(s) + s.calcAngularMomentum()
    finalAngVel.text = '\ndisk angular velocity: ' + str(s.w) + ' rad/s'
    finalAngMomentum.text = 'angular momentum: ' + str(totalAngularMomentum) + ' kg m²/s'
    gc.plot(t, b.calcEnergy(s) + s.calcEnergy())
    t += dt



scene.camera.follow(s.disk)
while True:
    rate(f)
    scene.camera.axis = vec(0,0,-1-s.disk.radius * 2.5)
    directionLabel.pos = vector(0, scene.range*0.9, 0)
    if (running):
        tick()
        if ((ccwBug and b.avel + b.decel * dt >= 0) or ((not ccwBug) and b.avel - b.decel * dt <= 0)):
            postSimulation = True
            b.avel = 0
