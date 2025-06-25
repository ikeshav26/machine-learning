from tkinter import *
import joblib
import numpy as np


model = joblib.load("jupyter/HeightToWeight.joblib")


def predictWeight():
    input=b.get()
    result=model.predict(np.array([[float(input)]]))
    d.config(text=f"Predicted weight: {result[0]} kg")
    b.delete(0, END)

root=Tk()
root.title("Height to weight predictor")
root.geometry("400x400")
root['bg'] = 'lightblue'


a=Label(root, text="Height to weight predictor", font=("Arial", 20), bg='lightblue')
a.pack(pady=20)

b=Entry(root, width=20, font=("Arial", 15))
b.pack(pady=10)

c=Button(root, text="Predict", font=("Arial", 15),  bg='lightgreen',command=predictWeight)
c.pack(pady=10)


d=Label(root, text="", font=("Arial", 15), bg='lightblue')
d.pack(pady=10)


root.mainloop()