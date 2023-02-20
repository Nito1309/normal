import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from scipy.stats import norm


def normal():
      
    file = pd.read_csv('data.csv')
    mean = file["edad"].mean()
    std = file["edad"].std()
    x = file["edad"].tolist()
    x.sort()
    x = np.linspace(mean - 3 * std, mean + 3 *std, 100)
    plt.plot(x, norm.pdf(x, mean, std),label="Distrubucion normal")
    plt.show()

window = tk.Tk()
window.title("Distribucion normal")
window.config(width=300, height=200)

btn = tk.Button(text="Ver distribucion", command=normal)
btn.place(x=100, y=100)

window.mainloop()