from tkinter import *
phoenix = Tk()

phoenix.title("Student Registration")
phoenix.geometry("900x900")

phoenix.configure(bg='blue')

def krish():
   print("YOUR PROFILE HAS BEEN CREATED ")
   print(f"{namevar.get() , stdvar.get() , batchvar.get() , rnvar.get() , passvar.get()}\n")

   with open("data.txt", "a") as f:
       f.write(f"{namevar.get() , stdvar.get() , batchvar.get() , rnvar.get() , passvar.get()}\n")

Label(phoenix, text="WELCOME TO PHOENIX E-LEARNING " , font= " Catamaran 20 " , bg="BLACK" , fg="white",padx=30,pady=20).grid(row = 0, column= 3)

# photo = PhotoImage(file="logo.jpg")
name = Label(phoenix, text="NAME :", bg='cyan')
std = Label(phoenix,text="CLASS :",bg='cyan')
batch = Label(phoenix,text="BATCH :",bg='cyan')
rn = Label(phoenix,text="STUDENT ID NUMBER :",bg='cyan')
password = Label(phoenix,text = "CREATE YOUR PASSWORD :",bg='cyan')


name.grid(row= 6, column=3 ,pady=10  )
std.grid(row= 7, column= 3,pady=10 )
batch.grid(row=8 , column= 3,pady=10)
rn.grid(row= 9, column= 3,pady=10 )
password.grid(row= 10, column= 3,pady=10 )


namevar = StringVar()
stdvar = StringVar()
batchvar = StringVar()
rnvar = StringVar()
passvar = StringVar()

nE = Entry(phoenix,textvariable=namevar)
sE = Entry(phoenix,textvariable=stdvar)
bE = Entry(phoenix,textvariable=batchvar)
rE = Entry(phoenix,textvariable=rnvar)
pE = Entry(phoenix,textvariable = passvar)


nE.grid(row= 6, column =4)
sE.grid(row= 7, column =4)
bE.grid(row= 8, column =4)
rE.grid(row= 9, column =4)
pE.grid(row= 10,column =4)




button = Button(phoenix,text= "CREATE A NEW PROFILE" , command = krish ).grid(row=23 , column = 4)






phoenix.mainloop()