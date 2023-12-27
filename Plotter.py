import json
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoLocator
from datetime import datetime

filename = 'data.json'

with open(filename, 'r') as f:
    data = json.load(f)

xvalues = sorted([data_x for data_x in data.keys()])
yvalues = [data[x_sorted] for x_sorted in xvalues]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.plot(xvalues, yvalues, linewidth=3)
current_time = datetime.now()
formatted_current_time = current_time.strftime('%d-%m-%Y %H:%M')
ax.set_title(f"File sizes over time / data for {formatted_current_time.expandtabs(12)}", fontsize=22)
ax.set_xlabel('Date [Y-m-d]', fontsize=16)
ax.set_ylabel('File size [MB]', fontsize=16)

ax.xaxis.set_major_locator(AutoLocator())
ax.yaxis.set_major_locator(AutoLocator())
ax.tick_params(axis='both', labelsize=12)

plt.savefig('plot.png')
plt.show()