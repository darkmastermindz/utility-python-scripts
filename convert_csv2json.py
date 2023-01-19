import pandas as pd
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

df = pd.read_csv(file_path)

json_path = filedialog.asksaveasfilename(defaultextension=".json")
df.to_json(json_path)

print("File successfully converted and saved!")
