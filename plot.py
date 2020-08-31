import matplotlib.pyplot as plt
import pandas as pd
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("fps", type=str, nargs="+")
args = parser.parse_args()

for i, fp in enumerate(args.fps):
    df = pd.read_csv(fp)
    plt.plot(df.iloc[:, 0], (df.iloc[:, 5]/3), color='C'+str(i), label="val-"+fp[:-4])
    plt.plot(df.iloc[:, 0], (df.iloc[:, 4]), color="C"+str(i), linestyle='dashed')
    
plt.xlim(right=140)
plt.ylim(top=200, bottom=0)
plt.xlabel("epochs")
plt.ylabel("loss")
plt.legend()
plt.savefig("test.png")