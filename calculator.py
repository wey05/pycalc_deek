import tkinter as tk

window = tk.Tk()
window.title('计算器wyx 1.1')
window.geometry('800x110+300+200')
window.resizable(False, False)

label=tk.Label(window,bg='pink',relief='raised')
label.place(x=0,y=0,width=800,height=110)

label=tk.Label(window, text='输入计算式：',bg='#d3fbfb',fg='red',font=('华文新魏',12),relief='raised')
label.place(x=20,y=5,width=100,height=40)

label=tk.Label(window, text='计算结果为：',bg='#d3fbfb',fg='red',font=('华文新魏',12),relief='raised')
label.place(x=20,y=65,width=100,height=40)

entry1=tk.Entry(window)
entry1.place(x=130,y=5,width=500,height=40)

def jisuan():
        result1.delete(1.0,'end')
        result=str(eval(entry1.get()))
        result1.insert(1.0,result)

button_addFile=tk.Button(window,text='开始计算',bg='#d3fbfb',fg='red',font=('华文新魏',12),relief='raised',command=jisuan)
button_addFile.place(x=650, y=30, width=120, height=40)

result1=tk.Text(window)
result1.place(x=130,y=65,width=500,height=40)

window.mainloop()