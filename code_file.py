import tkinter as tk

# Screen Setting
screen = tk.Tk()
screen.title("QR Code Maker")
screen.minsize(width="800",height="600")
screen.config(bg="gray")

# Label1
Label1 = tk.Label(screen, text="Enter the text you want to convert to a QR Code", font=("Arial",14,"bold"))
Label1.config(bg="gray", fg="orange")
Label1.pack(pady=10)

# Entry Setting
Entry = tk.Entry(width=60)
Entry.pack()

def Create_Qr_Code():
    user_input = Entry.get()
    pass

def Download_Qr_Code():
    pass

# Button_create Setting
Button_create = tk.Button(width=15,height=2, text="Create QR Code",font=("Arial",10,))
Button_create.pack(pady=20)

# Label for Qr Code
Label = tk.Label(width=40)
Label.pack(pady=80)

# Button_download Setting
Button_download = tk.Button(width=15,height=2, text="Download QR Code",font=("Arial",10,))
Button_download.pack()


screen.mainloop()