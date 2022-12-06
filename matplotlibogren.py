import matplotlib.pyplot as plt
import numpy as np
"""
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html sitenin linki.

x = [1,2,3,4]
y = [1,4,9,16]

#plt.plot(x,y , color = "Red") linewidth ile çizgi kalınlığı ayarlanabilir.
plt.plot(x , y , "o--r")
# -g olabilir . "--g" olabilir. birden fazla ifade gelebilir.
plt.axis([0,6,0,20])

plt.title("Baki Varol")
plt.xlabel("x ekseni")
plt.ylabel("y ekseni")"""
"""

x = np.linspace(0,2,100)


plt.plot(x , x , label = "linear" , color = "red")
plt.plot(x , x**2 , label = "quadratic" , color = "yellow")
plt.plot(x , x**3 , label = "cubic" , color = "green")

plt.xlabel("x ekseni")
plt.ylabel("y ekseni")

plt.title("grafik basligi")

plt.legend()

plt.show()
""""""
x = np.linspace(0,2,100)

#fig,axs = plt.subplots(3) ilk önrke için (3) kullanılmış.
fig,axs = plt.subplots(2,2)

axs[0].plot(x , x , color = "red")
axs[0].set_title("linear")

axs[1].plot(x , x**2 , color = "green")
axs[1].set_title("quadratic")

axs[2].plot(x , x**3 , color = "gray")
axs[2].set_title("cubic")

plt.tight_layout()

fig.suptitle("grafik basligi")

axs[0,0].plot(x , x , color = "red")
axs[0,1].plot(x , x**2 , color = "blue")
axs[1,0].plot(x , x**3 , color = "green")
axs[1,1].plot(x , x**4 , color = "yellow")
"""

import pandas as pd

df = pd.read_csv("all_seasons.csv")

df = df.drop(["draft_number"] , axis = 1).groupby("team_abbreviation").mean()

df.plot(subplots = True)
plt.legend()
plt.tight_layout()


plt.show()