import matplotlib.pyplot as plt 

up_lim = 1800 # Upper limit of the RPM
low_lim = 1400  # Lower limit of the RPM

v0 = 0
v1 = 35 # First gear speed = speed at 30 degree inclined plane 

v2 = (((up_lim - low_lim) * v1) / low_lim ) + v1
v3 = (((up_lim - low_lim) * v2) / low_lim ) + v2
v4 = (((up_lim - low_lim) * v3) / low_lim ) + v3

v5 = 165 # Top speed

maxRPM = (((v5-v4) * low_lim) / v4 ) + low_lim

# RPM values (y-axis)
rpm = [0, up_lim, low_lim, up_lim, low_lim, up_lim, low_lim, up_lim, low_lim, maxRPM]

# Corrseponding speed values (x-axis)
speed = [v0, v1, v1, v2, v2, v3, v3, v4, v4, v5]

# Plotting
plt.figure(figsize=(8,6))
plt.plot(speed, rpm, marker = 'x', linestyle='-' )
plt.title("Speed Vs. RPM")
plt.xlabel("RPM")
plt.xlabel("Speed (kmph)")
plt.grid(True)
plt.show()