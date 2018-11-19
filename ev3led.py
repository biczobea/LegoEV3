from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds

touch = TouchSensor()
led = Leds()

print("Nyomd meg a gombot, hogy megváltozzon a LED színe!")

while True:
    if touch.is_pressed:
        led.set_color("LEFT", "GREEN")
        led.set_color("RIGHT", "GREEN")

    else:
        led.set_color("LEFT" , "RED")
        led.set_color("RIGHT" , "RED")

#Ha megnyomom a gombot, akkor zöld lesz a led, ha nem akkor meg piros