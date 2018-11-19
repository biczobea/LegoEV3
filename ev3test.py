from ev3dev2.motor import LargeMotor, OUTPUT_A, SpeedPercent

motor = LargeMotor(OUTPUT_A)
motor.on_for_rotations(SpeedPercent(75), 5)

#A motor 75%-os sebességgel fordul ötöt