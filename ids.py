import argparse
import os

# Argument 

parser= argparse.ArgumentParser()
parser.add_argument("build", default=0, const=1)
parser.add_argument("checkout", default=0, const=1)
arg = parser.parse_args()

if arg.build == 1:
    print("build")

if arg.check == 1:
    print("check")

