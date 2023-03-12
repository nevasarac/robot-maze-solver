import tkinter as tk
import requests
#dosya 1 i okuma fonksiyonu
def oku1():
    dosya = requests.get("http://bilgisayar.kocaeli.edu.tr/prolab2/url1.txt")
    labirent["text"] = dosya.text

#dosya 2 yi okuma fonksiyonu
def oku2():
    dosya = requests.get("http://bilgisayar.kocaeli.edu.tr/prolab2/url2.txt")
    labirent["text"]=dosya.text

#gui açma yeri
pencere = tk.Tk()
pencere.title('proje')
pencere.geometry('750x750+550+150')

#buton 1 tanımlama yeri
buton=tk.Button(pencere,text='url1.txt',fg='white',background='black',command=oku1)
buton.place(
    x=50,
    y=30,
    height=30,
    width=60
)
#buton 2 tanımlama yeri
buton=tk.Button(pencere,text='url2.txt',fg='white',background='black',command=oku2)
buton.place(
    x=50,
    y=70,
    height=30,
    width=60
)

#text dosyasından çektiklerimizi yazma yeri
labirent=tk.Label(text="")
labirent.pack()

pencere.mainloop()





