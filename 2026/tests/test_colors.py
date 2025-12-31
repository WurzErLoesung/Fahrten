from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Color
from pybricks.tools import StopWatch, run_task, wait

from pupdevices import PupDevices

hub = PrimeHub()
pd = PupDevices()

print(f"\n{'='*40}")
print(f"System: {hub.system.name()}")
print(f"Batterie: {hub.battery.voltage()} mV")
print(f"Strom: {hub.battery.current()} mA")
print(f"{'='*40}\n")

Color.MAGENTA = Color(h=348, s=91, v=40)
Color.RED = Color(h=352, s=97, v=51)
Color.BLUE = Color(h=215, s=98, v=31)
Color.GREEN = Color(h=157, s=93, v=27)
Color.YELLOW = Color(h=52, s=79, v=70)
Color.WHITE = Color(h=118, s=13, v=75)
Color.NONE = Color(h=0, s=0, v=0)

colors = list(pd.color.detectable_colors())
colors.extend(
    [
        Color.MAGENTA,
        Color.RED,
        Color.BLUE,
        Color.GREEN,
        Color.YELLOW,
        Color.WHITE,
        Color.NONE,
    ]
)
pd.color.detectable_colors(colors)

while True:
    print(pd.color.color())
    wait(500)
