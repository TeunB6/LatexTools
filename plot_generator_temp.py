from src.utils import load_csv

data = load_csv("./plotdata.csv")

for r in data:
    if r != []:
        print(f"({r[0]}, {r[-2]}) +- ({0.1}, {r[-1]})")
