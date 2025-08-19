import tkinter as tk
from tkinter import filedialog
import qrcode
from PIL import Image, ImageTk

# Screen Setting
screen = tk.Tk()
screen.title("QR Code Maker")
screen.minsize(width="800",height="600")
screen.state("zoomed")
screen.config(bg="gray")
# Screen Panel
right_panel = tk.Frame(screen, width=400, bg="orange")
right_panel.pack(side="right", fill="y")

right_panel = tk.Frame(screen, width=400, bg="orange")
right_panel.pack(side="left", fill="y")

canvas = tk.Canvas(screen, width=800, height=400)
scrollbar = tk.Scrollbar(screen, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

# Label1
label_free=tk.Label(text="QR Code Maker" )
label_free.config(bg="gray",font=("Arial",20,"bold"))
label_free.pack(pady=20)
Label1 = tk.Label(screen, text="Enter the text you want to convert to a QR Code", font=("Arial",14,"bold"))
Label1.config(bg="gray", fg="orange")
Label1.pack(pady=12)

# Entry Setting
Entry = tk.Entry(width=60)
Entry.pack()

Qr_code_image = None      # Tkinter için PhotoImage
Qr_code_pil_image = None  # Kaydetmek için Pillow Image

def Create_Qr_Code():
    global user_input,Qr_code_pil_image
    user_input = Entry.get()
    if not user_input.strip(): # Boş entry kontrolü
        return

    # Qr Code Setting
    length = len(user_input)
    box_size = max(2, 10 - length // 20)
    qr = qrcode.QRCode(
        version=1,  # boyut
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,  # her kutucuk piksel boyutu
        border=4,  # kenar boşluğu
    )

    qr.add_data(user_input) # Qr kodu oluşturuyor
    qr.make(fit=True) # Eğer Qr kod boyutunda bir hata olursa (küçük gelirse) farklı boyutta qr oluşturur
    img = qr.make_image(fill_color="black", back_color="white")  # Qr kodu görsele döüştürür
    Qr_code_pil_image = img
    Qr_img = ImageTk.PhotoImage(img) # Labele eklemek için resim hale getirme

    # Label2 ye girilen metni ekeleme
    Label2.config(text=user_input)

    # Oluşan Qr kdou labelde gösterme
    Label_img.config(image=Qr_img)
    Label_img.image = Qr_img

    global Qr_code_image
    Qr_code_image=Qr_img

def Download_Qr_Code():
    global Qr_code_pil_image
    if Qr_code_pil_image :
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")],
            title="Download QR Code",
        )
        if file_path:
            Qr_code_pil_image.save(file_path)

# Button_create Setting
Button_create = tk.Button(width=15,height=2, text="Create QR Code",font=("Arial",10,),command=Create_Qr_Code)
Button_create.config(bg="#2b8778",)
Button_create.pack(pady=20)

# Label for Qr Code Name
Label2 = tk.Label(width=40, font=("Arial", 12, "bold"))
Label2.config(bg="#82ae56", fg="black")
Label2.pack()

# Label for Qr Code
Label_img = tk.Label(bg="gray")
Label_img.pack(pady=80)

# Button_download Setting
Button_download = tk.Button(width=15,height=2, text="Download QR Code",font=("Arial",10,),command=Download_Qr_Code)
Button_download.config(bg="#b28778",)
Button_download.pack()

screen.mainloop()