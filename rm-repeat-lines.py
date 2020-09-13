# this program will take a loss log and remove lines that repeat due to retraining
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("fp", type=str)
args = parser.parse_args()

with open(args.fp) as f:
    text = f.read()
    
newtext = []
i = 1
for line in text.split("\n"):
    if line == "":
        continue
    if int(line.split(",")[0]) >= i:
        i += 1
        newtext.append(line)
    else:
        newtext[int(line.split(",")[0]) - 1] = line
        print(i)
        
newtext = "\n".join(newtext) + "\n"
with open(args.fp[:-4] + "_fixed.txt", "w") as f:
    f.write(newtext)