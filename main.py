import Segment as sg
import RobotArm as ra
import numpy as np
'''
#Things to add:
So...kinda big problem. we dont want to delete and redraw the item each time when we can
just modify the points. 
We create a container for each segment that holds its line, cylinder,cube etc...We then specifically
modify these segments
#Current Bugs:
#The cylinder should overlap the lines not the other way around
'''

#Unit vectors in x,y,z direction for convenience 
ex = np.matrix([[1],[0],[0]])
ey = np.matrix([[0],[1],[0]])
ez = np.matrix([[0],[0],[1]])
#############################
#Create the segments that make up robot. Segment is initialized in the following form
# sg.Segment(type of joint, length, unit vector, zero configuration angle)
s3 = sg.Segment(0,0,ez,0)
s1 = sg.Segment(2,1.60,ez,0)
s6 = sg.Segment(0,0,ey,0)
s2 = sg.Segment(2,2.00,ez,0)
s7 = sg.Segment(1,1,ey,0)
s4 = sg.Segment(2,1.00,ex,0)

#Organize segments into a list, order matters!
segments = [s3,s1,s6,s2,s7,s4]
#Organize zero config angles, order matters!
Q = [-np.pi/4,0,0,0,0.5,0]

#construct robot arm from segment list and zero config list
r1 = ra.RobotArm(segments,Q)

#Specific Robots, Uncomment the section and comment everything else
##########################
#Rhino Arm
#s1 = sg.Segment(1,1,ex,0)
#s2 = sg.Segment(0,0,ez,0)
#s3 = sg.Segment(2,1,ez,0)
#s4 = sg.Segment(0,0,ey,0)
#s5 = sg.Segment(2,1,ex,0)
#s6 = sg.Segment(0,0,ey,0)
#s7 = sg.Segment(2,1,ex,0)
#s8 = sg.Segment(0,0,ey,0)
#s9 = sg.Segment(0,0,ex,0)
#s10 = sg.Segment(2,1,ex,0)

#segments = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]
#Q = [.2,0,0,0,0,0,0,0,0,0]

#r1 = ra.RobotArm(segments,Q)
##########################
#SCARA Robot
#s1 = sg.Segment(2,2,ez,0)
#s2 = sg.Segment(0,0,ez,0)
#s3 = sg.Segment(2,1,ex,0)
#s4 = sg.Segment(0,0,ez,0)
#s5 = sg.Segment(2,.25,-ez,0)
#s6 = sg.Segment(2,1,ex,0)
#s7 = sg.Segment(1,2,ez,0)
#s8 = sg.Segment(2,1,-ez,0)

#segments = [s1,s2,s3,s4,s5,s6,s7,s8]
#Q = [0,0,0,0,0,0,0,0]

#r1 = ra.RobotArm(segments,Q)
##########################
#Elbow Arm
#s1 = sg.Segment(2,2,ez,0)
#s2 = sg.Segment(0,0,ez,0)
#s3 = sg.Segment(0,0,ey,0)
#s4 = sg.Segment(0,0,ex,0)
#s5 = sg.Segment(2,1,ex,0)
#s6 = sg.Segment(0,0,ey,0)
#s7 = sg.Segment(2,1,ex,0)
#s8 = sg.Segment(0,0,ex,0)
#s9 = sg.Segment(2,1,ex,0)
#segments = [s1,s2,s3,s4,s5,s6,s7,s8,s9]
#Q = [0,0,0,0,0,0,0,0,0]

#r1 = ra.RobotArm(segments,Q)
###########################
#Dobot Arm V1.0
#s1 = sg.Segment(0,0,ez,0)
#s2 = sg.Segment(2,1,ez,0)
#s3 = sg.Segment(0,0,ey,0)
#s4 = sg.Segment(2,1.6,ez,0)
#s5 = sg.Segment(0,0,ey,0)
#s6 = sg.Segment(2,1.3,ex,0)

#segments = [s1,s2,s3,s4,s5,s6]
#Q = [0,0,0,0,0,0]

#r1 = ra.RobotArm(segments,Q)
