#!/usr/bin/env python3
'''Move the arm.'''

from wpilib.command import Command
from wpilib import XboxController
from wpilib.interfaces.generichid import GenericHID

class MoveArmWithTriggers(Command):
    '''Move the arm.'''
    def __init__(self, robot):
        '''Save the robot object, and pull in the arm subsystem.'''
        super().__init__()

        self.robot = robot
        self.requires(self.robot.arm)
        self.xbox0 = XboxController(0)

    def initialize(self):
        #Called just before this Command runs the first time
        pass
        

    def execute(self):
        #Called repeatedly when this Command is scheduled to run
        self.robot.arm.move(self.xbox0.getTriggerAxis(GenericHID.Hand.kLeft) +
            self.xbox0.getTriggerAxis(GenericHID.Hand.kRight)*-1)

        print (self.xbox0.getTriggerAxis(GenericHID.Hand.kLeft) + self.xbox0.getTriggerAxis(GenericHID.Hand.kRight)*-1)

    def isFinished(self):
        #Make this return true when this Command no longer needs to run execute()
        return self.isTimedOut()

    def end(self):
        #Called once after isFinished returns true
        pass

    def interrupted(self):
        '''Called when another Command which requires one or more of the same
        subsystems is scheduled to run
        '''
        self.end()
