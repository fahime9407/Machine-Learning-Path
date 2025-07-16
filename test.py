import math

v = float(input("Enter wind speed in kilometers/hour : "))
t = float(input("Enter air temperature in degrees celsius : "))

wci = 13.12 + 0.6215 * t - 11.37 * math.pow(v, 0.16) + 0.3965 * t * math.pow(v, 0.16)

print(f"I dont know wci!!!")

print(12 + "fahime")