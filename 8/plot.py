import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

with open("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split ("\n")]


data_array = np.loadtxt("data.txt", dtype=int)

size = np.shape(data_array)[0]
maximum = data_array.max()
maxIndex = np.where (data_array == maximum)
chargeTime = maxIndex[0][0] * tmp[0]
time2 = (size - maxIndex[0][0]) * tmp[0]

timeArr = np.arange(size) * tmp[0]

fig, ax = plt.subplots(figsize=(16, 10), dpi=400)
ax.plot(timeArr, data_array * tmp[1], 'o', linestyle='solid', markevery=15, linewidth=2, color='red', label="V(t)")

ax.set_ylim(0,3)
ax.set_xlim(0, 13)

ax.grid(which='minor', linewidth=0.5, linestyle='dashed')
ax.grid(which='major', linewidth=1)

ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))

ax.text(8.5, 2.0, f"Время заряда t = {chargeTime} c", fontsize=16)
ax.text(8.5, 1.8, f"Время разряда t = {time2} c", fontsize=16)

ax.set_xlabel("Время, c", fontsize=16)
ax.set_ylabel("Напряжение, B", fontsize=16)
ax.set_title("Процесс заряда и разряда конденсатора в RC-цепочке", fontsize=16)
ax.legend (fontsize=16, shadow=True, edgecolor="r", title="Legend")

fig.savefig("plot.png")