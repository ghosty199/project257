from tkinter import *
from web3 import Web3
from PIL import ImageTk, Image

root = Tk()
root.title("Account Details")

ganache_url = 'http://127.0.0.1:7545'

web3 = Web3(Web3.HTTPProvider(ganache_url))

img = ImageTk.PhotoImage(Image.open("image.png"))
panel = Label(root, image=img, bg='white')
panel.pack(side="top")

frame = Frame(
    root,
    bg='white',
    padx=5,
    pady=5
)
# create the labels to hold the account numbers
Label(frame,text="account number 1:", fg="black", bg= "white").grid(row=0, column=0, sticky=W, pady=10)
Label(frame,text="account number 2:", fg="black", bg= "white").grid(row=1, column=0, sticky=W, pady=10)
Label(frame,text="account number 3:", fg="black", bg= "white").grid(row=3, column=0, sticky=W, pady=10)
Label(frame,text="account number 4:", fg="black", bg= "white").grid(row=4, column=0, sticky=W, pady=10)
Label(frame,text="account number 5:", fg="black", bg= "white").grid(row=5, column=0, sticky=W, pady=10)
Label(frame,text="account number 6:", fg="black", bg= "white").grid(row=6, column=0, sticky=W, pady=10)






#Create entry elements to get the use input for account addresses 
account1 = Entry(frame).grid(row=0, column=1, sticky=W, pady=10)
account2 = Entry(frame).grid(row=1, column=1, sticky=W, pady=10)
account3 = Entry(frame).grid(row=2, column=1, sticky=W, pady=10)
account4 = Entry(frame).grid(row=3, column=1, sticky=W, pady=10)
account5 = Entry(frame).grid(row=4, column=1, sticky=W, pady=10)
account6 = Entry(frame).grid(row=5, column=1, sticky=W, pady=10)





#place the entry elements on the root window






#create the text box


#define a function CHECK_BALANCE() and add the code inside it.

    
   
  
    

    




       
     
        
      

frame.pack()

#Create a button element to call the CHECK_BALANCE()


    

result.pack(pady=5)
root.mainloop()

