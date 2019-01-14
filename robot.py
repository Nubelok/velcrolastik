#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on
"""

import wpilib
import wpilib.drive

from state import state
from oi import read_input
import timer
from oi import read_input_chasis
from oi import lift
from oi import cargo

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.left_motor = wpilib.Spark(0)
        self.right_motor = wpilib.Spark(1)
        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)
        
#self.timer = wpilib.Timer()

        self.lift_motor1 = wpilib.Spark(2)
        
        self.lift_motor2 = wpilib.Spark(3)
        
        #push
        self.lift_motor3 = wpilib.Spark(4)
        self.lift_motor4 = wpilib.Spark(5)
        self.lift_motor5 = wpilib.Spark(6)
        
        #sensor
        self.sensor1 = wpilib.DigitalInput(7)
        self.sensor2 = wpilib.DigitalInput(8)
    
    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        

        read_input()

        x = state ["chasis_x_mov"]
        y = state ["chasis_y_mov"] 

        self.drive.arcadeDrive(y, x)  
        

        if state["lift_up"]:

            
            state["timer"] += 1
            if self.sensor1.get() and self.sensor2.get(): 

                if state["timer"] >=1 and state["timer"] <= 50:

                    self.lift_motor1.set(0.5)
                    
                    self.lift_motor2.set(0)
                    self.lift_motor3.set(0) 
                    self.lift_motor4.set(0)
                    self.lift_motor5.set(0) 

                elif state["timer"] >= 50 and state["timer"] <=100:

                    self.lift_motor3.set(0.5) 
                    self.lift_motor4.set(0.5)
                    self.lift_motor5.set(0.5)
                    
                    self.lift_motor1.set(0)
                    self.lift_motor2.set(0)
                     
                elif state["timer"] >= 100 and state["timer"] <=150:
                    
                    self.lift_motor2.set(-0.5)
                    
                    self.lift_motor1.set(0)
                    self.lift_motor3.set(0) 
                    self.lift_motor4.set(0)
                    self.lift_motor5.set(0) 
                else:
                    self.lift_motor1.set(0)
                    self.lift_motor2.set(0)
                    self.lift_motor3.set(0) 
                    self.lift_motor4.set(0)
                    self.lift_motor5.set(0)   
            else:
                state["timer"] = 0



        cargo() #ISMAFEEDER 
        
        if state["cargo"]:
            self.cargo_motor.set(1)
        else:
            self.cargo_motor.set(0)

        lift()
        
        if state["lift"]:
            state["timer_lift"] += 1
            if state["timer_lift"] <= 50:
                self.lift_motor.set(1)
            elif state["timer_lift"] > 50 and state["timer_lift"] < 100:
                self.lift_motor.set(0)
                self.cargo_motor.set(-1)
            elif state["timer_lift"] >= 100:
                self.lift_motor.set(-1)
                self.cargo_motor.set(0)
        else:
            state["timer_lift"] = 0
            self.lift_motor.set(0)
        
            

    

if __name__ == "__main__":
    wpilib.run(MyRobot)