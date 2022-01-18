from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_server()
    down = str(round(sp.download()/(10**6),3))+"Mbps"
    up = str(round(sp.upload()/(10**6),3))+"Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)


sp = Tk()
sp.title("internet speed tester")
sp.geometry()
sp.config(bg="red")

lab = Label(sp,text="ineternet speed test", font=("Comforter Brush",30,"bold"))
lab.place(x=60,y=40,height=50,width=380)

lab_down = Label(sp,text="Download speed", font=("Comforter Brush",30,"bold"),bg="grey")
lab_down.place(x=60,y=130,height=50,width=380)

lab = Label(sp,text="00", font=("Comforter Brush",30,"bold"),bg="grey")
lab.place(x=60,y=200,height=50,width=380)

lab_up = Label(sp,text="Upload Speed", font=("Comforter Brush",30,"bold"),bg="grey")
lab_up.place(x=60,y=290,height=50,width=380)

lab = Label(sp,text="00", font=("Comforter Brush",30,"bold"),bg="grey")
lab.place(x=60,y=360,height=50,width=380)

button = Button(sp,text="Check Speed", font=("Time New Roman",30,"bold"),command=speedcheck)
button.place(x=60,y=460,height=50,width=380)

sp.mainloop()