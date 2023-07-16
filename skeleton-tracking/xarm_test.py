import xarm

# arm is the first xArm detected which is connected to USB
arm = xarm.Controller('USB')
print('Battery voltage in volts:', arm.getBatteryVoltage())

arm = xarm.Controller('USB')

servo2 = xarm.Servo(2, 500)       # assumes default unit position 500
servo3 = xarm.Servo(3, 500)       # assumes default unit position 500
servo4 = xarm.Servo(4, 500)       # assumes default unit position 500
servo5 = xarm.Servo(5, 500)       # assumes default unit position 500

# sets servo 1 to unit position 300 and waits the default 1 second
# before returning
arm.setPosition(2, 1000, duration=250, wait=True)
arm.setPosition(3, 870,duration=250, wait=True)
arm.setPosition(4, 500,duration=250, wait=True)
arm.setPosition(5, 1000,duration=250, wait=True)

arm.setPosition(2, 1000,duration=250, wait=True)
arm.setPosition(3, 1000,duration=250, wait=True)
arm.setPosition(4, 800,duration=250, wait=True)
arm.setPosition(5, 1000,duration=250, wait=True)

arm.setPosition(2, 1000,duration=250, wait=True)
arm.setPosition(3, 1000,duration=250, wait=True)
arm.setPosition(4, 1000,duration=250, wait=True)
arm.setPosition(5, 1000,duration=250, wait=True)

arm.setPosition(2, 1000,duration=250, wait=True)
arm.setPosition(3, 843,duration=250, wait=True)
arm.setPosition(4, 775,duration=250, wait=True)
arm.setPosition(5, 1000,duration=250, wait=True)

arm.setPosition(2, 1000,duration=250, wait=True)
arm.setPosition(3, 1000,duration=250, wait=True)
arm.setPosition(4, 1000,duration=250, wait=True)
arm.setPosition(5, 1000,duration=250, wait=True)

arm.setPosition(2, 1000,duration=250, wait=True)
arm.setPosition(3, 870,duration=250, wait=True)
arm.setPosition(4, 500,duration=250, wait=True)
arm.setPosition(5, 1000, duration=250, wait=True)



