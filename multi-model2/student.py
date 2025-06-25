from tkinter import *
import joblib


model= joblib.load("Score_predict.joblib")


def predict():
    hours= float(b.get())
    attendance= float(d.get())
    result=model.predict([[hours, attendance]])
    b.delete(0, END)
    d.delete(0, END)
    e.config(text=f"Predicted Score: {result[0]}")





root=Tk()
root.title("Score predictor")
root.geometry("400x500")
root['bg'] = 'lightblue'



head=Label(root,text="Score Predictor",bg='lightblue',font=("Arial", 24))
head.pack(pady=20)


a=Label(root,text="Hours you studies :",bg='lightblue',font=("Arial", 14))
a.pack(pady=20)

b=Entry(root,bg='lightblue',font=("Arial", 14))
b.pack(pady=10)


c=Label(root,text="Attendance Rate (%) :",bg='lightblue',font=("Arial", 14))
c.pack(pady=20)

d=Entry(root,bg='lightblue',font=("Arial", 14))
d.pack(pady=10)



f=Button(root,text="Predict Score",bg='lightblue',font=("Arial", 14),command=predict)
f.pack(pady=20)



e=Label(root,text="",bg='lightblue',font=("Arial", 14))
e.pack(pady=20)



root.mainloop()
