from tkinter import *
import joblib
from sklearn.preprocessing import PolynomialFeatures

root=Tk()
root['bg']='grey'
root.geometry("400x400")
root.title("Model 1")

poly=PolynomialFeatures(degree=3)

model=joblib.load('machine.joblib')

def predict():
    temp=float(entry1.get())
    prediction=model.predict(poly.fit_transform([[temp]]))
    entry1.delete(0, END)
    label.config(text=f"Predicted Efficiency: {prediction[0]:.2f} %")



head=Label(root,text="Machine Efficency Predictor",bg='grey',font=("Arial", 20))
head.pack(pady=20)

label1=Label(root,text="Enter temprature deviation:", bg='grey', font=("Arial", 14))
label1.pack(pady=10)

entry1=Entry(root, font=("Arial", 14))
entry1.pack(pady=10)

button1=Button(root, text="Predict", font=("Arial", 14), bg='lightblue',command=predict)
button1.pack(pady=20)

label=Label(root, text="", bg='grey', font=("Arial", 14))
label.pack(pady=10)

root.mainloop()