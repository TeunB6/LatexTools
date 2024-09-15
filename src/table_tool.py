import tkinter as tk
import sympy as sp
from tkinter.filedialog import askopenfilename
from io import BytesIO
from utils import load_csv
from table_maker import TableMaker
import PIL.Image as Image
import PIL.ImageTk as ImageTk
import os

class TableTool:
    def __init__(self) -> None:
        
        self.window = tk.Tk()
        self.window.geometry("1400x500")
        self.window.title("Latex Table Tool")
        self.window.withdraw()
        self.path = askopenfilename()
        self.window.deiconify()
        self.label = tk.Label(self.window)
        
        data = load_csv(self.path)
        
        self.table_maker = TableMaker(data)
        
        self.hor_lines_var = tk.BooleanVar(value=self.table_maker.draw_horizontal_lines)
        self.ver_lines_var = tk.BooleanVar(value=self.table_maker.draw_vertical_lines)
        
        hor_lines_check = tk.Checkbutton(self.window, variable=self.hor_lines_var, text="Draw Horizontal Lines", onvalue=True, offvalue=False)
        ver_lines_check = tk.Checkbutton(self.window, variable=self.ver_lines_var, text="Draw Vertical Lines", onvalue=True, offvalue=False)
        refresh_button = tk.Button(self.window, command=self.refresh, text='Refresh')
        save_button = tk.Button(self.window, command=self.save, text='Save')
        self._tex = "$a^2 + b^2 = c^2$"
        
        #Pack
        refresh_button.pack()
        save_button.pack()
        hor_lines_check.pack()
        ver_lines_check.pack()
        self.label.pack()
        
        self.refresh()
        self.window.mainloop()
    
    def refresh(self) -> None:
        # Update TableMaker
        self.table_maker.draw_horizontal_lines = self.hor_lines_var.get()
        self.table_maker.draw_vertical_lines = self.ver_lines_var.get()
        
        self._tex = self.table_maker.create_table()
        str_tex = ''.join(self._tex)
        f = BytesIO()
        sp.preview(str_tex, euler = False, viewer = "BytesIO", output = "ps", outputbuffer=f,
                   preamble=r"\documentclass{standalone}" + r"\begin{document}")
        f.seek(0)
        
        img = Image.open(f)
        
        img.load(scale=10)
        photo = ImageTk.PhotoImage(img)
        self.label.config(image = photo)
        self.label.image = photo
        f.close()
    
    def save(self) -> None:
        try:
            with open(f'{os.path.splitext(self.path)[0]}.txt', 'w') as f:
                f.writelines(self._tex)
        finally:
            pass

    
if __name__ == "__main__":
    lt = TableTool()
