from tkinter import *
import speedtest

def speedcheck():
    st = speedtest.Speedtest()
    st.get_servers()  
    down=str(round(st.download()/10**6,3))+" Mbps"
    up=str(round(st.upload()/10**6,3))+" Mbps"
    lab3.config(text=down)
    lab5.config(text=up)



st=Tk()
st.title("Internet Speed Tester")
st.geometry("400x600")
st.config(bg="Blue")
lab1 = Label(st,text="Internet Speed Tester",font=("Time New Roman",18,"bold"),bg="white",fg="Blue")
lab1.place(x=50,y=40,height=50,width=300)
lab2 = Label(st,text="Downloading Speed",font=("Time New Roman",18,"bold"),bg="white",fg="Blue")
lab2.place(x=50,y=150-20,height=50,width=300)
lab3 = Label(st,text="00",font=("Time New Roman",15,"bold"),bg="white",fg="Blue")
lab3.place(x=100,y=250-60,height=50,width=200)
lab4 = Label(st,text="Uploading Speed",font=("Time New Roman",18,"bold"),bg="white",fg="Blue")
lab4.place(x=50,y=350-50,height=50,width=300)
lab5 = Label(st,text="00",font=("Time New Roman",18,"bold"),bg="white",fg="Blue")
lab5.place(x=100,y=450-90,height=50,width=200)
lab6 = Button(st,text="Run Test",font=("Time New Roman",18,"bold"),bg="Green",fg="white",command=speedcheck)
lab6.place(x=50,y=550-80,height=50,width=300)

st.mainloop()

