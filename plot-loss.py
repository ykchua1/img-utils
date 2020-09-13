import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import pandas as pd
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("fps", type=str, nargs="+")
args = parser.parse_args()

fig, ax = plt.subplots()

for i, fp in enumerate(args.fps):
    df = pd.read_csv(fp)
    ax.plot(df.iloc[:, 0], (df.iloc[:, 5]/3), color='C'+str(i), label="val-"+fp[:-4])
    ax.plot(df.iloc[:, 0], (df.iloc[:, 4]), color="C"+str(i), linestyle='dashed')
    
minorlocator = AutoMinorLocator(5)
ax.xaxis.set_minor_locator(minorlocator)
ax.yaxis.set_minor_locator(minorlocator)
ax.grid(which='both')
ax.set_xlim(left=0, right=200)
ax.set_ylim(top=200, bottom=0)
ax.set_xlabel("epochs")
ax.set_ylabel("loss")
ax.legend()
fig.savefig("test.png")