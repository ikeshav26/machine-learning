from tkinter import *
import joblib
import numpy as np



model = joblib.load("jupyter/cgpacal.joblib")


def calculate():
    input_value=b.get()
    result=model.predict(np.array([[float(input_value)]]))
    b.delete(0, END)
    d.config(text=f"Predicted Package: {result[0]:.2f} LPA", bg="White", fg="Black", font=("Arial", 15))




root=Tk()
root['bg']="Black"
root.title("Package Calculator")
root.geometry("300x300")



a=Label(root,text="Package Calculator",bg="White",fg="Black",font=("Arial",20))
a.grid(row=0,column=0,columnspan=3,padx=15,pady=10)

b=Entry(root,bg="white",fg="Black",font=("Arial",15))
b.grid(row=1,column=0,columnspan=3,padx=15,pady=20)


c=Button(root,text="Calculate",bg="Green",fg="Black",font=("Arial",15),command=calculate)
c.grid(row=2,column=0,columnspan=3,padx=10,pady=20)


d=Label(root,text="Your predicted package",bg="White",fg="Black",font=("Arial",15))
d.grid(row=3,column=0,columnspan=3,padx=10,pady=10)




root.mainloop()