import csv
def load_csv(path: str) -> list:
    with open(path) as file:
        csv_reader = csv.reader(file)
        data = [[c.strip() for c in row] for row in csv_reader]
    return data