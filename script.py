import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", required=True)
parser.add_argument("-o", "--output", required=True)
parser.add_argument("-t", "--temp", required=True)
args = parser.parse_args()

with open(os.path.join(args.output, "result.txt"), "w") as f:
    f.write("done\n")
