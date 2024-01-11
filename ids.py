import argparse
import os

# Argument 

parser= argparse.ArgumentParser()
parser.add_argument("build")
parser.add_argument("checkout")
arg = parser.parse_args()

if arg[1] == "build":
    print("build") 

if arg[1] == "check":
    print("check")

