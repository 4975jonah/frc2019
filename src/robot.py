#!/usr/bin/python3
'''robot.py: The "main" line of the code.'''

import math
import wpilib
from commandbased import CommandBasedRobot
from wpilib.command import Scheduler
from subsystems.drivetrain import DriveTrain
from subsystems.puncher import Puncher
from subsystems.rear_puncher import RearPuncher
from subsystems.claw import Claw
from subsystems.arm import Arm
from subsystems.intake import Intake
from oi import OI
from subsystems.elevator import Elevator
from wpilib.cameraserver import CameraServer
from subsystems.hatch import Hatch
from subsystems.intake_winch import IntakeWinch

class MyRobot(CommandBasedRobot):
    '''Primary class, the Periodic methods in which are called
    repeatedly by the RoboRIO system service.'''

    def robotInit(self):
        '''Initialize all subsystems.'''
        self.drivetrain = DriveTrain(self)
        self.puncher = Puncher()
        self.rear_puncher = RearPuncher()
        self.claw = Claw()
        self.arm = Arm()
        self.intake = Intake()
        self.elevator = Elevator()
        self.hatch = Hatch()
        self.intake_winch = IntakeWinch()
        #self.camera0=CameraServer.launch()

        self.oi = OI(self)

    def disabledInit(self):
        '''Initialize systems when entering Disabled Mode.'''

    def disabledPeriodic(self):
        '''Called approximately every 20ms while in Disabled Mode.'''
        return super().disabledPeriodic()

    def autonomousInit(self):
        '''Initialize systems when entering Autonomous Mode.'''

    def autonomousPeriodic(self):
        '''Called approximately every 20ms while in Autonomous Mode.'''
        Scheduler.getInstance().run()

    def teleopInit(self):
        '''Initialize systems when entering Teleoperated Mode.'''

    def teleopPeriodic(self):
        '''Called approximately every 20ms while in Teleoperated Mode.'''
        Scheduler.getInstance().run()

    def testInit(self):
        '''Initialize systems when entering Test Mode.'''

    def testPeriodic(self):
        '''Called approximately every 20ms while in Test Mode.'''
        Scheduler.getInstance().run()

if __name__ == "__main__":
    '''Kick off the robot code.'''
    wpilib.run(MyRobot)
