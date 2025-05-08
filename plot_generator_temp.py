from src.utils import load_csv
from tkinter.filedialog import askopenfilename

data = load_csv(askopenfilename())

for r in data:
    if r != []:
        print(f"({r[1]}, {r[-2]}) +- ({r[2]}, {r[-1]})")
