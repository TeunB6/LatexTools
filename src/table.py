import csv
import sys
import os

ADD_LINES = True

def latex_table_csv(path: str) -> str:
    with open(path) as file:
        csv_reader = csv.reader(file)
        table = [[c.strip() for c in row] for row in csv_reader]
    row_len = len(table[0])
    print(table)
    table_latex = ["\\begin{tabular} {" + ("c " * row_len) + '}\n']
    for row in table:
        print([f" {c} &" for c in row[:-1]])

        row_latex = ''.join(f"{c} &" for c in row[:-1]) + f"{row[-1]} \\\\ \n"
        if ADD_LINES:
            row_latex += "\hline \n"
        table_latex.append(row_latex)
    table_latex.append("\\end{tabular\}")
    
    with open(f'{os.path.splitext(path)[0]}.txt', 'w') as f:
        f.writelines(table_latex)
    

if __name__ == "__main__":
    path = sys.argv[1]
    latex_table_csv(path)
    