from tkinter import *

def bmi_compute():
    w=float(weight.get())
    h=float(height.get())/100.0
    bmi=w/(h*h)
    answer='당신의 체질량 지수(BMI)는: {:4.2f}'.format(bmi)
    result.config(text=answer)

window=Tk()
label=Label(window,text='체중(kg)과 키(cm)를 차례로 입력하세요')
label.pack()

weight=Entry(window,width=50)
weight.pack()
height=Entry(window,width=50)
height.pack()
button=Button(window, text='BMI 계산',command=bmi_compute)
button.pack()
result=Label(window, text='당신의 체질량 지수 (BMI)는:')
result.pack()
window.mainloop()