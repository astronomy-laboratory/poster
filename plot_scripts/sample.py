import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import golden

plt.style.use("paper_sty.mplstyle")

width = 3.46  # inches
height = width / golden

# let's generate some random function
x = np.random.normal(0, .5, 1000)

fig, ax = plt.subplots(figsize=(width, height))
ax.hist(x, label="data")
ax.legend(loc="upper right")
ax.set_xlabel("$x$-axis")
ax.set_ylabel("$y$-axis")

fig.tight_layout()
fig.savefig("../figures/sample.pdf")