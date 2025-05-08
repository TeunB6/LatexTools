class TableMaker:
    def __init__(self, data: list) -> None:
        self._draw_horizontal_lines = False
        self._draw_vertical_lines = False
        self.data = data
        self.row_len = len(self.data[0])
        
    def create_table(self) -> list[str]:
        print("Creating Table with Settings: " + f"Hor: {self._draw_horizontal_lines}; Ver: {self._draw_vertical_lines}")
        table_latex = (["\\begin{tabular} {" + "c | " * (self.row_len - 1) + "c" + '}\n'] if self._draw_vertical_lines
                        else  ["\\begin{tabular} {" + ("c " * self.row_len) + '}\n'])
        for row in self.data:
            row_latex = ''.join(f"{c} & " for c in row[:-1]) + f"{row[-1]} \\\\ \n"
            if self._draw_horizontal_lines:
                row_latex += "\hline \n"
            table_latex.append(row_latex)
        table_latex.append("\\end{tabular}")
        return table_latex
    
    @property
    def draw_horizontal_lines(self) -> bool:
        self._draw_horizontal_lines
    
    @draw_horizontal_lines.setter
    def draw_horizontal_lines(self, new_val) -> bool:
        self._draw_horizontal_lines = bool(new_val)
    
    @property
    def draw_vertical_lines(self) -> bool:
        self._draw_vertical_lines
    
    @draw_vertical_lines.setter
    def draw_vertical_lines(self, new_val) -> bool:
        self._draw_vertical_lines = bool(new_val)
        