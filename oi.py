import wpilib
from state import state
from wpilib.buttons import JoystickButton 

def read_input ():
	stick = wpilib.Joystick(1)
	#izquierda y dercha
	y = stick.getY()
	x = stick.getX()
	#up and dowm
	a = stick.getRawButton(1)
	b = stick.getRawButton(2)
	#push
	c = stick.getRawButton(3)
	#timer
	e = stick.getRawButton(4)
	
	state["chasis_y_mov"] = y
	state["chasis_x_mov"] = x
	state["lift_up"] = e

def cargo(): #ISMAFEEDER
	stick = wpilib.Joystick(1)

	button_1_is_pressed = stick.getRawButton(5)
	state["cargo"] = button_1_is_pressed
	
def lift(): #ISMAFEEDER

	stick = wpilib.Joystick(1)
	
	button_2_is_pressed = stick.getRawButton(6)
	state["lift"] = button_2_is_pressed
	

