from tkinter import *
import joblib
from sklearn.preprocessing import PolynomialFeatures

model=joblib.load('poly-model2/model2.joblib')
poly=PolynomialFeatures(degree=3)

def predict():
    input=float(entry1.get())
    prediction=model.predict(poly.fit_transform([[input]]))
    entry1.delete(0, END)  
    label_result.config(text=f"Predicted Productivity: {prediction[0]:.2f} ")

root=Tk()
root['bg']='lightblue'
root.geometry("400x400")
root.title("Productivity Predictor")


head=Label(root,text="Productivity Predictor",bg='lightblue',font=("Arial", 20))
head.pack(pady=20)

label=Label(root, text="Enter the sleep deviation:", bg='lightblue', font=("Arial", 14))
label.pack(pady=10)

entry1=Entry(root, font=("Arial", 14))
entry1.pack(pady=10)


button1=Button(root, text="Predict", font=("Arial", 14), bg='lightgreen',command=predict)
button1.pack(pady=20)

label_result=Label(root, text="", bg='lightblue', font=("Arial", 14))
label_result.pack(pady=10)


root.mainloop()