import pandas as pd
import tkinter as tk
from tkinter import filedialog
import os

def open_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    if not os.path.isfile(file_path):
        print("Invalid file path")
        exit()
    return file_path

def save_file(df):
    json_path = filedialog.asksaveasfilename()
    if json_path[-5:] != '.json':
        json_path += '.json'
    if not json_path:
        print("Invalid file path")
        exit()
    df.to_json(json_path)
    print("File successfully converted and saved!")

file_path = open_file()
df = pd.read_csv(file_path)
save_file(df)
