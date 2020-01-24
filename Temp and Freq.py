from gpiozero import CPUTemperature
from time import sleep, strftime, time
import matplotlib.pyplot as plt
import subprocess

plt.ion()
x = []
y = []
z = []
i=0;

cpu = CPUTemperature()
with open("/home/pi/cpu_temp.csv", "a") as log:
    while True:
        temp = cpu.temperature
        test=subprocess.Popen(["vcgencmd measure_clock arm"], shell=True, stdout=subprocess.PIPE)
        output=test.communicate()[0]
        output=output.decode("utf-8") #encoding byte string to ascii string
        output=int(output[14:]) # string to int
        freq = output/1000000000
        y.append(temp)
        x.append(i)
        z.append(freq)
        plt.clf()
        plt.subplot(2,1,1)
        plt.plot(x,y)
        plt.subplot(2,1,2)
        plt.plot(x,z)
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d: %H:%M:%S"),str(temp)))
        plt.pause(1)
        i=i+1
        print(i)
        plt.draw()
        if i > 30:
                     x.pop(0);
                     y.pop(0);
                     z.pop(0);