from tkinter import *
import joblib
import numpy as np



model=joblib.load("jupyter/model3.joblib")


def  caluclate():
    input=b.get()
    result=model.predict(np.array([[float(input)]]))
    d.config(text=f"Predicted marks: {result[0]}")
    b.delete(0, END)

root=Tk()
root.title("Marks predictor")
root.geometry("400x300")
root['bg'] = 'lightpink'    


a=Label(root, text="Marks predictor", font=("Arial", 20), bg='lightpink')
a.pack(pady=20)

b=Entry(root, width=20, font=("Arial", 15))
b.pack(pady=10)

c=Button(root, text="Predict", font=("Arial", 15),  bg='lightgreen',command=caluclate)
c.pack(pady=10)

d=Label(root, text="", font=("Arial", 15), bg='lightpink')
d.pack(pady=10)





root.mainloop()