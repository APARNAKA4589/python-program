from tkinter import*
def buttonClick(number):
    global operator
    operator=operator+str(number)
    input_value.set(operator)

def buttonClear():
    global operator
    operator=""
    input_value.set("")

def buttonEqual():
    global operator
    result=str(eval(operator))
    input_value.set(result)
    operator=""


main= Tk()
main.title("Calculator")

operator=""
input_value=StringVar()
display_text=Entry(main,font=("arial",20,"bold"),textvariable=input_value,bd=30,insertwidth=4,
                   bg="powder blue",justify=RIGHT)
display_text.grid(columnspan=4)

#row1
btn_7=Button(main,padx=16,fg="purple",font=("arial",20,"bold"),text="7",command=lambda:buttonClick("7"))
btn_7.grid(row=1,column=0)
btn_8=Button(main,padx=16,fg="red",font=("arial",20,"bold"),text="8",command=lambda:buttonClick("8"))
btn_8.grid(row=1,column=1)
btn_9=Button(main,padx=16,fg="yellow",font=("arial",20,"bold"),text="9",command=lambda:buttonClick("9"))
btn_9.grid(row=1,column=2)
btn_10=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="+",command=lambda:buttonClick("+"))
btn_10.grid(row=1,column=3)

#row2
btn_11=Button(main,padx=16,fg="blue",font=("arial",20,"bold"),text="4",command=lambda:buttonClick("4"))
btn_11.grid(row=2,column=0)
btn_12=Button(main,padx=16,fg="violet",font=("arial",20,"bold"),text="5",command=lambda:buttonClick("5"))
btn_12.grid(row=2,column=1)
btn_13=Button(main,padx=16,fg="orange",font=("arial",20,"bold"),text="6",command=lambda:buttonClick("6"))
btn_13.grid(row=2,column=2)
btn_14=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="-",command=lambda:buttonClick("-"))
btn_14.grid(row=2,column=3)

#row3
btn_15=Button(main,padx=16,fg="brown",font=("arial",20,"bold"),text="1",command=lambda:buttonClick("1"))
btn_15.grid(row=3,column=0)
btn_16=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="2",command=lambda:buttonClick("2"))
btn_16.grid(row=3,column=1)
btn_17=Button(main,padx=16,fg="chocolate",font=("arial",20,"bold"),text="3",command=lambda:buttonClick("3"))
btn_17.grid(row=3,column=2)
btn_18=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="",command=lambda:buttonClick(""))
btn_18.grid(row=3,column=3)

#row4
btn_19=Button(main,padx=16,fg="navyblue",font=("arial",20,"bold"),text="0",command=lambda:buttonClick("0"))
btn_19.grid(row=4,column=0)
btn_20=Button(main,padx=16,fg="indigo",font=("arial",20,"bold"),text="c",command=lambda:buttonClear())
btn_20.grid(row=4,column=1)
btn_21=Button(main,padx=16,fg="teal",font=("arial",20,"bold"),text="=",command=lambda:buttonEqual())
btn_21.grid(row=4,column=2)
btn_22=Button(main,padx=16,fg="black",font=("arial",20,"bold"),text="/",command=lambda:buttonClick("/"))
btn_22.grid(row=4,column=3)





main.mainloop()