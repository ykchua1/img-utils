import cv2
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("fp")
parser.add_argument("angle", type=int)

args = parser.parse_args()
fname = os.path.basename(args.fp).split(".")[0]

assert args.angle in [90, 180, 270]
assert os.path.isfile(fname + '.txt')

im = cv2.imread(args.fp)
if args.angle == 90:
    im = cv2.rotate(im, cv2.ROTATE_90_COUNTERCLOCKWISE)
    print("rotated by 90 deg")
elif args.angle == 180:
    im = cv2.rotate(im, cv2.ROTATE_180)
    print("rotated by 180 deg")
else:
    im = cv2.rotate(im, cv2.ROTATE_90_CLOCKWISE)
    print("rotated by 270 deg")
new_fname = fname+"_rot_"+str(args.angle)
cv2.imwrite(new_fname+".jpg", im)

# rotate the text file as well
with open(fname + ".txt") as f:
    text = f.readlines()

def transform_line(line, angle):
    line = line.split()
    line = [float(x) for x in line]
    if angle == 270:
        line[1], line[2] = -line[2]+1.0, line[1]
        line[3], line[4] = line[4], line[3]
    elif angle == 180:
        line[1], line[2] = -line[1]+1.0, -line[2]+1.0
    else:
        line[1], line[2] = line[2], -line[1]+1.0
        line[3], line[4] = line[4], line[3]
    line = ["{:.6f}".format(x) if i!=0 else str(int(x)) for i, x in enumerate(line)]
    line = " ".join(line) + "\n"
    return line

for i, line in enumerate(text):
    newline = transform_line(line, args.angle)
    text[i] = newline
    
with open(new_fname+".txt", "w") as f:
    f.write("".join(text))