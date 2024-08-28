import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import os

# görüntüleri pdfe dönüştürme işlevi

def images_to_pdf(images, pdf_name):
    try:
        # yeni bir pdf dosyası oluştur
        pdf = Image.open(images[0])
        pdf.save(pdf_name, "PDF", resolution = 100.0,
                 save_all = True, append_images=images[1:])
        messagebox.showinfo("Başarılı",
                            "Resimler başarıyla PDF'e dönüştürüldü.")
    except Exception as e:
        messagebox.showerror("Error",
                              "Resimleri PDF'e dönüştürme işlemi başarısız oldu.\nEroor: " + str(e))
# resimleri seçme işlevi

def select_images():
    images:filedialog.askopenfilenames(title= "Seçili Resimler",
                                       filetypes=(("Resim uzantıları","*.jpg;*.jpeg;*.png"),
                                        ("Tüm dosyalar", "*.*")),initaldir = "C:/")                    
                                         return images

# PDF adını ve yolunu seçme işlevi

def select_pdf():
        pdf = filedialog.asksaveasfilename(title= "PDF olarak kaydet",
                                           defaultextension= ".pdf", initaldir = "C:/",
                                           filetypes=(("PDF Dosyaları", "*.pdf"), ("Tüm Dosyalar", "*.*")))
        return pdf

# GUİ oluştur

root = tk.Tk()
root.title("Resimleri PDF'e dönüştür")
select_images_btn = tk.Button(root,
                              text = "Resim Seç", command = select_images)
select_pdf_btn = tk.Button(root, text= "PDF Seç",
                           command=select_pdf)
convert_btn = tk.Button(root, text="Dönüştür",
                        command=lambda: images_to_pdf(select_images(),select_pdf()))
select_images_btn.pack()
select_pdf_btn.pack()
convert_btn.pack()
root.mainloop()