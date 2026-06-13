#Very-Buggy-Spinner! (pun intended)
#By: Michael Lee & Lucas Long
#
#Project Description:
#Our simulation is based on Problem 44 from the Angular Momentum problem set. The problem features a Texas-sized cockroach that is running on a lazy susan and comes to a stop.
#Our simulation similarly features a rotating ladybug and spinner, but with more customizability.
#Through adjusting various parameters like angular velocities, masses, and angular acceleration of the ladybug, we can use conservation of angular momentum to model how the system changes.
#
#Instructions:
#Once you run the program, you will see a gray spinner and a red ladybug.
#
#Below are eight separate sliders, each with a label to the side of it. By adjusting the value of a slider (click and drag), you adjust the value of the corresponding parameter in the label.
#For example, by adjusting the slider labeled “mass of disk”, you will change the value of the mass of the disk when the simulation is run.
#
#The eight sliders are as follows:
#
#mass of disk: This changes the mass of the disk/spinner
#mass of bug: This changes the mass of the ladybug
#disk initial angular velocity: This changes the angular velocity of the disk at the start of the simulation
#bug initial angular velocity: This changes the angular velocity of the ladybug at the start of the simulation relative to the disk
#(Note: For both the disk and the bug, positive values of initial angular velocity correspond to rotation in the clockwise direction)
#
#disk radius: This changes the radius of the disk/spinner
#bug deceleration: This changes the magnitude of the angular acceleration of the ladybug
#(Note: regardless of the initial direction of the ladybug’s rotation, acceleration will be in the opposite direction to slow down the ladybug)
#
#bug radial distance: This changes the distance of the ladybug from the center of the disk
#bug initial angle: This changes the starting angle of the ladybug on the disk
#
#
#
#At the very top, there is a button titled “start simulation” and a button titled “reset”
#
#If you click the “start simulation” button,  the simulation will begin using the current values of each of the sliders. Assuming that the initial angular velocities aren’t set to 0, this will mean the spinner and ladybug will begin rotating.
#(Note: While the simulation is running, the sliders cannot be adjusted)
#Additionally, whenever the simulation is running, there will be an updating graph that displays the kinetic energy of the spinner/ladybug system versus time. There are also two lines that display the last measured angular velocity of the spinner and the last measured angular momentum of the system.
#
#If you click the “reset” button, the simulation will stop, assuming that it is currently running. This will enable the sliders again, allowing you to adjust them if desired.
