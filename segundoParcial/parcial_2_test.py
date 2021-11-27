import os
from os.path import isfile, join
"""Script to test all givenn problems at once"""
cwd=os.getcwd()
problemas=[join(cwd, f) for f in os.listdir(cwd) if (isfile(join(cwd, f)) and str(f).split("_")[0]=="problema")]

if __name__=="__main__":
    for i, j in enumerate(problemas):
        print("////////////////////////////////////////////////////////////////////////////////////")
        print(f"Test Problema N°{i+1}")
        os.system(f"python {j}")
        print("///////////////////////////////////////////////////////////////////////////////////")